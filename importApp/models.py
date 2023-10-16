from django.db import models

# Create your models here.
#Clase Pedido que representa información sobre un pedido.

class Pedido(models.Model):
    nombre_articulo = models.CharField(max_length=100)
    codigo_articulo = models.CharField(max_length=20)
    proveedor = models.CharField(max_length=100)
    cantidad_unidades = models.PositiveIntegerField()
    costo_unitario_usd = models.DecimalField(max_digits=10, decimal_places=2)
    costo_envio_usd = models.DecimalField(max_digits=10, decimal_places=2)