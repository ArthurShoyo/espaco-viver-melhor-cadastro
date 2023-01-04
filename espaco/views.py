from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_date

from .models import Atendimentos, Pessoa


# Create your views here.
def home(request):
    return render(request, 'espaco/pages/home.html')
@login_required(login_url='/usuarios')
def painel(request):
    if request.method != 'POST':
        return render(request, 'espaco/pages/cadastro.html')
    nome = request.POST.get('name')
    cpf = request.POST.get('cpf')
    datanascimento = request.POST.get('datenasc')
    profissao = request.POST.get('profissao')
    endereco = request.POST.get('endereco')
    cidade = request.POST.get('cidade')
    uf = request.POST.get('uf')
    pais = request.POST.get('pais')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    genero = request.POST.get('gender')
    obsrecepcao = request.POST.get('obsrecepcao')
    idade = request.POST.get('idade')
    filhos = request.POST.get('filhos')
    opcaosexual = request.POST.get('opcaosexual')
    doencadiagnosticadas = request.POST.get('doencadiagnosticadas')
    fazusomedicamentos = request.POST.get('fazusomedicamentos')
    obs_terapeuta = request.POST.get('obs_terapeuta')
    obs_complementar = request.POST.get('obs_complementar')
    Pessoa.objects.create(nome=nome, cpf=cpf, datenasc=datanascimento, profissao=profissao, endereco=endereco, cidade=cidade, uf=uf, pais=pais, email=email, telefone=telefone, genero=genero, obsrecepcao=obsrecepcao, idade=idade, filhos=filhos, opcaosexual=opcaosexual, doencadiagnosticada=doencadiagnosticadas, fazusodemedicamentos=fazusomedicamentos, obsterapeuta=obs_terapeuta, obscomplementares=obs_complementar)
    return render(request, 'espaco/pages/cadastro.html')

@login_required(login_url='/usuarios')
def clientes(request):
    cliente = Pessoa.objects.order_by('-id')
    return render(request, 'espaco/pages/clientes.html', {
        'clientes': cliente
    })
@login_required(login_url='/usuarios')
def ver_cliente(request, pessoa_id):
    cliente = Pessoa.objects.get(id=pessoa_id)
    return render(request, 'espaco/pages/ver_clientes.html', {
        'cliente': cliente
    })
@login_required(login_url='/usuarios')
def excluircliente(request, pessoa_id):
    cliente = Pessoa.objects.get(id=pessoa_id)
    cliente.delete()
    return redirect('espaco:clientes')
@login_required(login_url='/usuarios')
def editarcliente(request, pessoa_id):
    cliente = Pessoa.objects.get(id=pessoa_id)    
    return render(request, 'espaco/pages/update.html', {
        'cliente': cliente
    })
@login_required(login_url='/usuarios')
def update(request, pessoa_id):
    vnome = request.POST.get('name')
    vcpf = request.POST.get('cpf')
    vdatanascimento = parse_date(request.POST.get('datenasc'))
    vprofissao = request.POST.get('profissao')
    vendereco = request.POST.get('endereco')
    vcidade = request.POST.get('cidade')
    vuf = request.POST.get('uf')
    vpais = request.POST.get('pais')
    vemail = request.POST.get('email')
    vtelefone = request.POST.get('telefone')
    vgenero = request.POST.get('gender')
    vobs = request.POST.get('obsrecepcao')
    vidade = request.POST.get('idade')
    vfilhos = request.POST.get('filhos')
    vopcaosexual = request.POST.get('opcaosexual')
    vdoencadiagnosticadas = request.POST.get('doencadiagnosticadas')
    vfazusomedicamentos = request.POST.get('fazusomedicamentos')
    vobs_terapeuta = request.POST.get('obs_terapeuta')
    vobs_complementar = request.POST.get('obs_complementar')
    cliente = Pessoa.objects.get(id=pessoa_id)
    cliente.nome = vnome
    cliente.cpf = vcpf
    cliente.datenasc = vdatanascimento
    cliente.profissao = vprofissao
    cliente.endereco = vendereco
    cliente.cidade = vcidade
    cliente.uf = vuf
    cliente.pais = vpais
    cliente.email = vemail
    cliente.telefone = vtelefone
    cliente.genero = vgenero
    cliente.obsrecepcao = vobs
    cliente.idade = vidade
    cliente.filhos = vfilhos
    cliente.opcaosexual = vopcaosexual
    cliente.doencadiagnosticada = vdoencadiagnosticadas
    cliente.fazusodemedicamentos = vfazusomedicamentos
    cliente.obsterapeuta = vobs_terapeuta
    cliente.obscomplementares = vobs_complementar
    cliente.save()
    return redirect('espaco:clientes')
@login_required(login_url='/usuarios')
def meusatendimentos(request):
    atendimento = Atendimentos.objects.order_by('-id')
    return render(request, 'espaco/pages/meusatendimentos.html', {
        'atendimentos': atendimento
    })

@login_required(login_url='/usuarios')
def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        raise Http404()
    cliente = Pessoa.objects.order_by('-id').filter(
        Q(nome__icontains=termo) | Q(cpf=termo) | Q(telefone=termo)
    )
    return render(request, 'espaco/pages/busca.html', {
        'clientes': cliente
    })
@login_required(login_url='/usuarios')
def buscaatend(request):
    busca = request.GET.get('busca')
    if busca is None or not busca:
        raise Http404()
    
    atendimento = Atendimentos.objects.order_by('-id').filter(
        Q(nome__icontains=busca) | Q(tecnicaaplicada__icontains=busca)
    )
    return render(request, 'espaco/pages/buscaatend.html', {
        'atendimentos': atendimento
    })
@login_required(login_url='/usuarios')
def novoatend(request):
    if request.method != ('POST'):
        return render(request, 'espaco/pages/novoatendimento.html')
    nome = request.POST.get('name')
    cpf = request.POST.get('cpf')
    tecnicaaplicada = request.POST.get('tecnicaaplicada')
    tempoconsulta = request.POST.get('tempoconsulta')
    queixaprincipal = request.POST.get('queixaprincipal')
    tipoconsulta = request.POST.get('tipoconsulta')
    tempoqueixa = request.POST.get('tempoqueixa')
    medicamentos = request.POST.get('medicamentos')
    obsatend = request.POST.get('obsatend')
    Atendimentos.objects.create(nome=nome, cpf=cpf, tecnicaaplicada=tecnicaaplicada, queixaprincipal=queixaprincipal, tempoconsulta=tempoconsulta, tipoconsulta=tipoconsulta, medicamentos=medicamentos, tempoqueixa=tempoqueixa, obsatend=obsatend)
    return redirect('espaco:meusatendimentos')
@login_required(login_url='/usuarios')
def veratendimento(request, atendimento_id):
    atendimento = Atendimentos.objects.get(id=atendimento_id)
    return render(request, 'espaco/pages/veratendimento.html', {
        'atendimento': atendimento
    })
@login_required(login_url='/usuarios')
def excluiratendimento(request, atendimento_id):
    atendimento = Atendimentos.objects.get(id=atendimento_id)
    atendimento.delete()
    return redirect('espaco:meusatendimentos')

def editaratendimento(request, atendimento_id):
    atendimento = Atendimentos.objects.get(id=atendimento_id)    
    return render(request, 'espaco/pages/atendupdate.html', {
        'atendimento': atendimento
    })

@login_required(login_url='/usuarios')
def atendupdate(request, atendimento_id):
    vnome = request.POST.get('name')
    vcpf = request.POST.get('cpf')
    vtecnicaaplicada = request.POST.get('tecnicaaplicada')
    vtempoconsulta = request.POST.get('tempoconsulta')
    vqueixaprincipal = request.POST.get('queixaprincipal')
    vtempoqueixa = request.POST.get('tempoqueixa')
    vtipoconsulta = request.POST.get('tipoconsulta')
    vmedicamentos = request.POST.get('medicamentos')
    vobsatend = request.POST.get('obsatend')
    atendimento = Atendimentos.objects.get(id=atendimento_id)
    atendimento.nome = vnome
    atendimento.cpf = vcpf
    atendimento.tecnicaaplicada = vtecnicaaplicada
    atendimento.medicamentos = vmedicamentos
    atendimento.tempoconsulta = vtempoconsulta
    atendimento.queixaprincipal = vqueixaprincipal
    atendimento.tempoqueixa = vtempoqueixa
    atendimento.tipoconsulta = vtipoconsulta
    atendimento.obsatend = vobsatend
    atendimento.save()
    return redirect('espaco:meusatendimentos')
