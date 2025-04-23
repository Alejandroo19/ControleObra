from django.db import models
from django.utils.timezone import now


class Obra(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('andamento', 'Andamento'),
            ('finalizada', 'Finalizada'),
        ],
        default='andamento'
    )
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    def verificar_status(self):
        soma_valores = sum(valor.valor for valor in self.valores_adicionados.all())
        if soma_valores >= self.valor and self.status != 'finalizada':
            self.status = 'finalizada'
            self.save()
            
class ValorAdicionado(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('dinheiro', 'Dinheiro'),
        ('credito', 'Cartão de Crédito'),
        ('debito', 'Cartão de Débito'),
    ]
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='valores_adicionados')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True) 
    data = models.DateTimeField(default=now)
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO_CHOICES)

    def __str__(self):
        return f"{self.obra.nome} - R$ {self.valor}"

class ValorObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='valores_obra')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.obra.nome} - Valor específico"
    

class FuncionarioObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='funcionarios')
    nome = models.CharField(max_length=255)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    data_adicionado = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.nome} ({self.obra.nome})"
