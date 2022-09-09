"""principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import inicio, detalleVenta
from compra.views import CompraListView, FacturaCompraListView, DetaCompra, ActualizarCliente, EliminarCompra
from venta.views import VentaListView, crearVenta, ActualizarVenta, FacturaVentaListView, EliminarVenta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('venta/', VentaListView.as_view(), name='venta'),
    path('crearventa/', crearVenta.as_view(), name='crearventa'),
    path('detalleventa/',detalleVenta,name='detalleVenta'),
    path('compra/', CompraListView.as_view(), name='compra'),
    path('crearcompra/', DetaCompra.as_view(), name='crearcompra'),
    path('actualizarcompra/<int:pk>/', ActualizarCliente.as_view(), name='actualizarcompra'),
    path('detallecompra/<int:pk>',FacturaCompraListView.as_view(),name='detalleCompra'),
    path('deletecompra/<int:pk>/', EliminarCompra.as_view(), name='deletecompra'),
    path('actualizarventa/<int:pk>/', ActualizarVenta.as_view(), name='actualizarventa'),
    path('detalleventa/<int:pk>', FacturaVentaListView.as_view(), name='detalleventa'),
    path('deleteventa/<int:pk>/', EliminarVenta.as_view(), name='deleteventa'),
]
