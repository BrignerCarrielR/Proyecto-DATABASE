from django.shortcuts import render

# Create your views here.
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)

def detalleVenta(request):
  data = {
      'titulo':'DETALLE DE LA VENTA',
      'action':'add',
      'listar_url': '/compra',
  }
  return render(request, "ventas/detalleventa.html",data)

