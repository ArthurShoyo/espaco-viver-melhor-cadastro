from django.db import models


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    datenasc = models.CharField(max_length=12, blank=True, null=True)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    uf = models.CharField(max_length=40, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=25, blank=True, null=True)
    obsrecepcao = models.TextField(blank=True, null=True)
    filhos = models.CharField(max_length=25, blank=True, null=True)
    idade = models.CharField(max_length=15, blank=True, null=True)
    opcaosexual = models.CharField(max_length=20, blank=True, null=True)
    doencadiagnosticada = models.CharField(max_length=40, blank=True, null=True)
    fazusodemedicamentos = models.CharField(max_length=40, blank=True, null=True)
    obsterapeuta = models.TextField(blank=True, null=True)
    obscomplementares = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome



class Atendimentos(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=20)
    tecnicaaplicada = models.CharField(max_length=100, blank=True, null=True)
    queixaprincipal = models.CharField(max_length=100, blank=True, null=True)
    tempoconsulta = models.CharField(max_length=20, blank=True, null=True)
    tempoqueixa = models.CharField(max_length=100, blank=True, null=True)
    tipoconsulta = models.CharField(max_length=20, blank=True, null=True)
    dataatend = models.DateField(auto_now=True)
    medicamentos = models.CharField(max_length=50, blank=True, null=True)
    obsatend = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.nome)


    
