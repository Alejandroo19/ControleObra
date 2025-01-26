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
