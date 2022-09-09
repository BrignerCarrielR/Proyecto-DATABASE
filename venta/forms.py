from django import forms
from django.forms import ModelForm
from venta.models import  DetVenta


class DetVentaForm(ModelForm):
    class Meta:
        model = DetVenta
        fields = ['venta','licor','cantidad']
        widgets = {
            'venta': forms.Select(attrs={'class': 'form-control'}),
            'licor': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }