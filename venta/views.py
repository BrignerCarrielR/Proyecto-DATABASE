from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

from venta.forms import DetVentaForm
from venta.models import Venta, DetVenta


# Create your views here.

class crearVenta(CreateView):
    model = DetVenta
    template_name = "ventas/crearventa.html"
    success_url = reverse_lazy('venta')
    form_class = DetVentaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = ''
        context['titulo'] = 'NUEVA VENTA'
        context['url_anterior'] = ''
        context['listar_url'] = '/venta'
        context['action'] = 'add'
        return context

class VentaListView(ListView):
    template_name = "ventas/lisventas.html"
    context_object_name = 'ventas'
    model = DetVenta
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancelar_url']= '/'
        context['crear_url'] = '/crearventa'
        context['titulo'] = 'LISTADO DE VENTAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class ActualizarVenta(UpdateView):
    model = DetVenta
    template_name = "ventas/crearventa.html"
    success_url = reverse_lazy('venta')
    form_class = DetVentaForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE VENTA'
        context['listar_url'] = '/venta'
        return context

class EliminarVenta(DeleteView):
    model = DetVenta
    template_name = "ventas/deleteventa.html"
    success_url = reverse_lazy('venta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE VENTA'
        context['listar_url'] = '/venta'
        return context

class FacturaVentaListView(DeleteView):
    model = DetVenta
    template_name = "ventas/detalleventa.html"
    success_url = reverse_lazy('venta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'DETALLE DE VENTA'
        context['listar_url'] = '/venta'
        return context