from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InvCab(models.Model):
    id_inv = models.BigAutoField(primary_key=True)  # Cambiado a BigAutoField para autoincrementar
    store = models.CharField(max_length=3)
    nota_inv = models.CharField(max_length=100, blank=True, null=True)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con User
    estado = models.IntegerField(default=0)
    estado_conteo = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inventario {self.id_inv} - Tienda {self.store}"

class InvConteo(models.Model):
    id_inv = models.ForeignKey(InvCab, on_delete=models.CASCADE)  # Relación con InvCab
    zona = models.IntegerField()
    cod_plano = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Conteo para Inv {self.id_inv.id_inv} - Zona {self.zona}"

class InvDet(models.Model):
    id = models.AutoField(primary_key=True)
    id_inv = models.ForeignKey(InvCab, on_delete=models.CASCADE)  # Relación con InvCab
    zona = models.IntegerField()
    sku = models.CharField(max_length=20)
    linea = models.IntegerField()
    modelo = models.CharField(max_length=13)
    color = models.TextField()
    talla = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50)
    temp_comercial = models.CharField(max_length=10)
    familia = models.CharField(max_length=10)
    marca = models.CharField(max_length=10, blank=True, null=True)
    cantidad = models.IntegerField()
    username = models.CharField(max_length=21)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Detalle de Inv {self.id_inv.id_inv} - SKU {self.sku}"
