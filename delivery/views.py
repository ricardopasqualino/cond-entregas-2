from asyncio import tasks
from django.shortcuts import render, redirect
from core.form import NovaForm, DeliveryForm
from delivery.models import Delivery, Morador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail


@login_required
def Morador(request):
    return render (request, 'delivery/morador.html')
    
@login_required
def Home(request):
    return render(request, 'delivery/index.html')


@login_required
def Nova(request):
    form = NovaForm()
    return render(request, 'delivery/nova.html', {'form': form})


@login_required
def Entrega_nova(request):
    form = NovaForm(request.POST or None)
    if form.is_valid():
        form.save()
    #     send_mail (
    #     'Você tem uma nova entrega!', 
    #     'Chegou! Sua encomenda está na portaria te esperando.', 
    #     'importados@efprodutosdigitais.com.br', 
    #     ['ricardo.pasqualino@gmail.com'],
    # ) 
        return redirect('Entregas')
    else:
        return redirect('Erro')


@login_required
def Entregas(request):
    entregas = Delivery.objects.order_by('-data_entrada').all()
    return render(request, 'delivery/entregas.html', {'entregas': entregas})


@login_required
def Atualizar_entrega(request, id):
    data = {}
    entrega = Delivery.objects.get(id=id)
    form = DeliveryForm(request.POST or None, instance=entrega)
    data['entrega'] = entrega
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Entregas')
    else:
        return render (request, 'delivery/atualizar_entrega.html', data)


@login_required
def Box(request):
    return render (request, 'delivery/box.html')


@login_required
def Casa(request):
    return render(request, 'delivery/casas.html')


def Login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main_index')
    else:
        return redirect('erro')


@login_required
def Logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


@login_required
def Password_reset(request):
    return render(request, 'accounts/password_reset.html')


@login_required
def Register(request):
    return render(request, 'accounts/register.html')


@login_required
def Morador_novo(request):
    form = NovaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Entregas')
    else:
        return redirect('Erro')


@login_required
def Erro(request):
    return render(request, 'erro.html')


def Painel(request):
    # x  = Delivery.objects.all()
    # qtd_entregas = x.count()
    return render(request, 'delivery/painel.html')



