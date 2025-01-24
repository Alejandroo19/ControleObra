from django.db import models

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

    def __str__(self):
        return self.nome
