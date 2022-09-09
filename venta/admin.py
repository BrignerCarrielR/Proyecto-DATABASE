from django.contrib import admin

from venta.models import DetVenta,Venta


# Register your models here.
class VentaAdmin (admin.ModelAdmin):
    list_display = ['cliente','fecha']
    search_fields = ['tipoLicor']
    list_per_page = 15
class DetVentaAdmin(admin.ModelAdmin):
    list_display = ['licor','venta','cantidad','total']
    search_fields = ['licor']
    list_per_page = 15
# Register your models here.
admin.site.register(Venta,VentaAdmin)
admin.site.register(DetVenta,DetVentaAdmin)