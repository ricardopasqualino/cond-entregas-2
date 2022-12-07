
from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include
from delivery.views import ( 
    Home, 
    Casa, 
    Morador,
    Morador_novo, 
    Nova, 
    Entrega_nova, 
    Entregas, 
    Login_view, 
    Logout_view, 
    Password_reset, 
    Atualizar_entrega,
    Erro,
    Painel,
    Register,
)

from main.views import index

from guests.views import (
    visitantes, 
    eventos, 
    listas, 
    guest_home, 
    novo_evento, 
    criar_evento, 
    novo_visitante,
    criar_visitante,
    atualizar_evento,
    atualizar_visitante,
    deletar_visitante,
    deletar_evento,
)

from parking.views import parking, reserva_vagas

urlpatterns = [
    #admin Django
    path('admin/', admin.site.urls, name='Admin'),
    
    #Delivery
    path('delivery/', Home, name='delivery_home'),
    path('casa/', Casa, name='Casa'),
    path('morador/', Morador, name='Morador'),
    path('nova/', Nova , name='Nova'),
    path('entrega-nova/', Entrega_nova , name='Entrega_nova'),
    path('atualizar-entrega-<id>/', Atualizar_entrega , name='Atualizar_entrega'),
    path('entregas/', Entregas , name='Entregas'),
    path('erro/', Erro , name='Erro'),

    # -- Guests -- #

        #Home
    path('guests/', guest_home , name='guests_home'),

        #Convidados
    path('convidados/', visitantes , name='guests_convidado'),
    path('novo-convidado/', novo_visitante , name='guests_novo_convidado'),
    path('criar-convidado/', criar_visitante , name='guests_criar_convidado'),
    path('atualizar-convidado/(?P<id>\d+)/$', atualizar_visitante , name='guests_editar_convidado'),
    path('deletar-convidado/(?P<id>\d+)/$', deletar_visitante , name='guests_deletar_convidado'),
    path('lista-convidados/', listas , name='guests_lista'),


        #Eventos
    path('eventos/', eventos , name='guests_evento'),
    path('novo-evento/', novo_evento , name='guests_novo_evento'),
    path('criar-evento/', criar_evento , name='guests_criar_evento'),
    path('atualizar-evento/(?P<id>\d+)/$', atualizar_evento , name='guests_atualizar_evento'),
    path('deletar-evento/<id>', deletar_evento , name='guests_deletar_evento'),

    # -- Parking -- #
    path('parking/', parking , name='parking_home'),
    path('reservar-vaga/', reserva_vagas , name='parking_vaga'),
    
    #Autentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', Login_view , name='Login'),
    path('logout/', Logout_view , name='Logout'),
    path('reset-senha/', Password_reset , name='Password_reset'),
    path('cadastro/', Morador_novo , name='Morador_novo'),
    path('acesso/', Register , name='Register'),

    #Main
    path('', index , name='main_index'),

    
    #Painel
    path('painel/', Painel , name='Painel'),
]