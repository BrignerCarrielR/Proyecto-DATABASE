from django.db import models

from app.models import Proveedor, Licor


# Create your models here.

# Create your models here.
class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha=models.DateField(blank=False, null=True)
    total=models.FloatField(default=0)
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['id']

    def __str__(self):
        return "{} - {}".format(self.id, self.proveedor)

class DetCompra(models.Model):
    id = models.AutoField(primary_key=True)
    licor = models.ForeignKey(Licor, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    total = models.FloatField(blank=False, null=True)

    class Meta:
        verbose_name = "DetCompra"
        verbose_name_plural = "DetCompras"
        ordering = ['id']

    def __str__(self):
        self.total = self.cantidad * self.licor.precio
        return "{}".format(self.total)

    # @property
    # def suma_valores(self):
    #     return (self.licor.precio + self.cantidad)
    # def save(self):
    #     self.compra.total=self.suma_valores
    #     super (Compra, self).save()
