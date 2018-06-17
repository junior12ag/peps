from django.db import models

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)



class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=50)
    video = models.CharField(max_length=500, blank=True)
    vacuna = models.ManyToManyField(Vacuna, blank=True)
    foto = models.ImageField(upload_to="fotos", blank=True)
    estado = models.BooleanField(default = False)

    def __str__(self):
        return '{}'.format(self.nombre)
