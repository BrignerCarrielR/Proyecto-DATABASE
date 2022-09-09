from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.template import Context

from compra.forms import CompraForm, DetCompraForm
# Create your views here.
from compra.models import DetCompra, Compra
from app.models import Licor

class DetaCompra(CreateView):
    model = DetCompra
    template_name = "compras/crearcompra.html"
    success_url = reverse_lazy('compra')
    form_class = DetCompraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'NUEVA C0MPRA'
        context['url_anterior'] = ''
        context['listar_url'] = '/compra'
        # context['action'] = 'add'
        # formulario=context['action']
        # print(formulario)
        return context

class CompraListView(ListView):
    template_name = "compras/liscompra.html"
    context_object_name = 'compras'
    model = DetCompra
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
        context['crear_url'] = '/crearcompra'
        context['titulo'] = 'LISTADO DE COMPRAS'
        context['query'] = self.request.GET.get("query") or ""
        return context


class ActualizarCliente(UpdateView):
    model = DetCompra
    template_name = "compras/crearcompra.html"
    success_url = reverse_lazy('compra')
    form_class = DetCompraForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DE COMPRA'
        context['listar_url'] = '/venta'
        return context

class EliminarCompra(DeleteView):
    model = DetCompra
    template_name = "compras/delete.html"
    success_url = reverse_lazy('compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR DE COMPRA'
        context['listar_url'] = '/compra'
        return context

class FacturaCompraListView(DeleteView):
    model = DetCompra
    template_name = "compras/detallecompra.html"
    success_url = reverse_lazy('compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'DETALLE DE COMPRA'
        context['listar_url'] = '/compra'
        return context

# class FacturaListView(ListView):
#     template_name = "compras/detallecompra.html"
#     context_object_name = 'facturas'
#     model = DetCompra
#
#     def get_queryset(self):
#         query = self.request.GET.get("query")
#         print(query)
#         if query:
#             return self.model.objects.filter(nombres__icontains=query)
#         else:
#             return self.model.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['url_anterior'] = ''
#         context['listar_url'] = '/compra'
#         context['crear_url'] = ''
#         context['titulo'] = 'FACTURA DE LA COMPRA'
#         context['query'] = self.request.GET.get("query") or ""
#         return context
