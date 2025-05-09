# Generated by Django 5.1.4 on 2025-01-26 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_obra_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValorObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField()),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valores', to='obras.obra')),
            ],
        ),
    ]
