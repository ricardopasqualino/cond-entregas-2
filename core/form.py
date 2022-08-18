from django.forms import ModelForm
from delivery.models import Delivery
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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