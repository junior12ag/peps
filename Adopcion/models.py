from django.db import models
from Mascota.models import Mascota

# Create your models here.

class SolicitudAdopcion(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    identificacion = models.CharField(max_length=20)
    direccion = models.TextField()
    razon = models.TextField()
    fecha = models.DateField()
    mascota = models.ForeignKey(Mascota, null=True, blank=True)
    telefono = models.CharField(max_length=12)
    ocupacion = models.TextField()
    estado = models.NullBooleanField()
