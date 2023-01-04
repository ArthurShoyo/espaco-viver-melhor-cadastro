from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'usuarios/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, 'Usuario ou senha invalidos')
        return render(request, 'usuarios/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Voce fez login com sucesso')
        return redirect('espaco:painel')
        
def logout(request):
    auth.logout(request)
    return render(request, 'usuarios/login.html')

