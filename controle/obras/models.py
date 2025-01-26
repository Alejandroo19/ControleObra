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

class ValorAdicionado(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='valores_adicionados')  # Nome único para o relacionamento
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)  # Campo de descrição
    data = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.obra.nome} - R$ {self.valor}"

class ValorObra(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='valores_obra')  # Nome único para o relacionamento
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.obra.nome} - Valor específico"
