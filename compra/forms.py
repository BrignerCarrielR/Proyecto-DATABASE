from django import forms
from django.forms import ModelForm
from compra.models import Compra,DetCompra

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DetCompraForm(ModelForm):
    class Meta:
        model = DetCompra
        fields = ['compra','licor','cantidad']
        widgets = {
            'compra': forms.Select(attrs={'class': 'form-control'}),
            'licor': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }