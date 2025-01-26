from django.db import models

class Obra(models.Model):
    nome = models.CharField(max_length=255)  # Nome da obra
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da obra
    status = models.CharField(
        max_length=20,
        choices=[
            ('andamento', 'Andamento'),
            ('finalizada', 'Finalizada'),
        ],
        default='andamento'
    )
    descricao = models.TextField(blank=True, null=True)  # Descrição da obra

    def __str__(self):
        return self.nome
    
    def valor_total_adicionado(self):
        total = sum(valor.valor for valor in self.valores.all())
        return total

    def atualizar_status(self):
        if self.valor_total_adicionado() >= self.valor:
            self.status = 'finalizada'
            self.save()


class ValorObra(models.Model):
    obra = models.ForeignKey(Obra, related_name='valores', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.valor} - {self.descricao[:50]}"
