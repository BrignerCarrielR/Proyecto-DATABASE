from django.db import models

from app.models import Empleado, Cliente, Licor


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha=models.DateField(blank=False, null=True)
    total=models.FloatField(default=0)
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['id']

    def __str__(self):
        return "{} - {}".format(self.id,self.cliente)

class DetVenta(models.Model):
    id = models.AutoField(primary_key=True)
    licor = models.ForeignKey(Licor, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    total = models.FloatField(blank=False, null=True)

    class Meta:
        verbose_name = "DetVenta"
        verbose_name_plural = "DetVentas"
        ordering = ['id']

    def __str__(self):
        self.total = self.cantidad * self.licor.precio
        return "{}".format(self.total)