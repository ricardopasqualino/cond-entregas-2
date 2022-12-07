from django.shortcuts import render
from parking.models import vagas
from django.contrib.auth.decorators import login_required


@login_required
def parking(request):
    vagas_dados = vagas.objects.all()
    data = {'vagas_dados' : vagas_dados}
    return render(request, 'parking/home.html', data)


@login_required
def reserva_vagas(request):
    return render (request, 'parking/vagas.html')
