from django.contrib import admin
from .models import Cliente, tipoEmpleado, Empleado, Proveedor, tipoLicor, Licor


# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','cedula','telefono','correo','direccion']
    search_fields = ['nombre']
    list_per_page = 10

class tipoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ['tipoEmpleado','sueldo']
    search_fields = ['tipoEmpleado']
    list_per_page = 10

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','tipoEmpleado']
    search_fields = ['nombre']
    list_per_page = 10

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre','ruc','telefono','direccion']
    search_fields = ['nombre']
    list_per_page = 10

class tipoLicorAdmin(admin.ModelAdmin):
    list_display = ['id','tipoLicor']
    search_fields = ['tipoLicor']
    list_per_page = 10
class LicorAdmin(admin.ModelAdmin):
    list_display = ['nombre','tipoLicor','stock','precio']
    search_fields = ['nombre']
    list_per_page = 10

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(tipoEmpleado,tipoEmpleadoAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(tipoLicor,tipoLicorAdmin)
admin.site.register(Licor,LicorAdmin)


