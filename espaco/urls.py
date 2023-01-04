from django.urls import path

from . import views

app_name = 'espaco'

urlpatterns = [
    path('', views.home),
    path('painel/', views.painel, name='painel'),
    path('clientes/', views.clientes, name='clientes'),
    path('verclientes/<int:pessoa_id>', views.ver_cliente, name='ver_cliente'),
    path('delete/<int:pessoa_id>', views.excluircliente, name='excluircliente'),
    path('editar/<int:pessoa_id>', views.editarcliente, name="editarcliente"),
    path('update/<int:pessoa_id>', views.update, name="update"),
    path('atendimentos/', views.meusatendimentos, name="meusatendimentos"),
    path('busca/', views.busca, name='busca'),
    path('buscaatend/', views.buscaatend, name='buscaatend'),
    path('novoatendimento/', views.novoatend, name='novoatend'),
    path('veratendimento/<atendimento_id>', views.veratendimento, name='veratendimento'),
    path('excluiratendimento/<atendimento_id>', views.excluiratendimento, name='excluiratendimento'),
    path('atendeditar/<int:atendimento_id>', views.editaratendimento, name="editaratendimento"),
    path('atendupdate/<int:atendimento_id>', views.atendupdate, name="atendupdate"),
    


]
