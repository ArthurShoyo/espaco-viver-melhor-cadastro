# Generated by Django 4.1.4 on 2022-12-30 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espaco', '0003_alter_atendimentos_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentos',
            name='obsatend',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atendimentos',
            name='queixaprincipal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='atendimentos',
            name='tecnicaaplicada',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='atendimentos',
            name='tempoconsulta',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='atendimentos',
            name='tempoqueixa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
