# Generated by Django 4.1.4 on 2023-01-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espaco', '0004_alter_atendimentos_obsatend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimentos',
            name='tipoconsulta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
