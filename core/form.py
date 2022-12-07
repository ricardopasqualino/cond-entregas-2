from django.forms import ModelForm
from delivery.models import Delivery
from guests.models import evento, convidado


class NovaForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 


class MoradorForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'


class NovoEventoForm(ModelForm):
    class Meta:
        model = evento
        fields = '__all__'


class NovoVisitanteForm(ModelForm):
    class Meta:
        model = convidado
        fields = '__all__'
