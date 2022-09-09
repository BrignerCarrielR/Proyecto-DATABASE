from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    cedula = models.CharField(max_length=10,unique=True, blank=False, null=True)
    telefono = models.CharField(max_length=10,unique=True, blank=False, null=True)
    correo = models.EmailField(max_length=100,unique=True,blank=False, null=True)
    direccion = models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.nombre)

class tipoEmpleado(models.Model):
    id= models.AutoField(primary_key=True)
    tipoEmpleado = models.CharField(max_length=100,unique=True, blank=False, null=True)
    sueldo = models.FloatField(unique=True, blank=False, null=True)

    class Meta:
        verbose_name = "Tipo de Empleado"
        verbose_name_plural = "Tipos de Empleados"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.tipoEmpleado)


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    tipoEmpleado=models.ForeignKey(tipoEmpleado,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    telefono = models.CharField(max_length=10,unique=True, blank=False, null=True)


    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.nombre)

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    ruc = models.CharField(max_length=10, unique=True, blank=False, null=True)
    telefono = models.CharField(max_length=10,unique=True, blank=False, null=True)
    direccion=models.CharField(max_length=100, blank=False, null=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.nombre)

class tipoLicor(models.Model):
    id = models.AutoField(primary_key=True)
    tipoLicor = models.CharField(max_length=100,unique=True, blank=False, null=True)
    class Meta:
        verbose_name = "Tipo de Licor"
        verbose_name_plural = "Tipoes de Licores"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.tipoLicor)

class Licor(models.Model):
    id = models.AutoField(primary_key=True)
    tipoLicor = models.ForeignKey(tipoLicor, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=100,unique=True, blank=False, null=True)
    stock=models.IntegerField(default=0)
    precio=models.FloatField(blank=False, null=True)
    class Meta:
        verbose_name = "Licor"
        verbose_name_plural = "Licores"
        ordering = ['tipoLicor']

    def __str__(self):
        return "{}".format(self.nombre)

