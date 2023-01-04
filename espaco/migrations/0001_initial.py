# Generated by Django 4.1.4 on 2022-12-28 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=20)),
                ('datenasc', models.CharField(blank=True, max_length=12)),
                ('profissao', models.CharField(blank=True, max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=100)),
                ('cidade', models.CharField(blank=True, max_length=60)),
                ('uf', models.CharField(blank=True, max_length=40)),
                ('pais', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('genero', models.CharField(blank=True, max_length=25)),
                ('obsrecepcao', models.TextField(blank=True)),
                ('filhos', models.CharField(blank=True, max_length=25, null=True)),
                ('idade', models.CharField(blank=True, max_length=15, null=True)),
                ('opcaosexual', models.CharField(blank=True, max_length=20, null=True)),
                ('doencadiagnosticada', models.CharField(blank=True, max_length=40, null=True)),
                ('fazusodemedicamentos', models.CharField(blank=True, max_length=40, null=True)),
                ('obsterapeuta', models.TextField(blank=True, null=True)),
                ('obscomplementares', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Atendimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=20)),
                ('tecnicaaplicada', models.CharField(max_length=100)),
                ('queixaprincipal', models.CharField(max_length=100)),
                ('tempoconsulta', models.CharField(max_length=20)),
                ('tempoqueixa', models.CharField(max_length=100)),
                ('dataatend', models.DateField(auto_now=True)),
                ('obsatend', models.TextField()),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='espaco.pessoa')),
            ],
        ),
    ]
