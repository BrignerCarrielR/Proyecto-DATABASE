from django.contrib import admin

from compra.models import DetCompra,Compra

class CompraAdmin (admin.ModelAdmin):
    list_display = ['proveedor','fecha','total']
    search_fields = ['tipoLicor']
    list_per_page = 15
class DetCompraAdmin(admin.ModelAdmin):
    list_display = ['licor','compra','cantidad','total']
    search_fields = ['licor']
    list_per_page = 15
# Register your models here.
admin.site.register(Compra,CompraAdmin)
admin.site.register(DetCompra,DetCompraAdmin)