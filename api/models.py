from django.db import models
from django.contrib.auth.models import User

class Casa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    longitud = models.DecimalField(null=True, max_digits=8, decimal_places=5)
    latitud = models.DecimalField(null=True, max_digits=8, decimal_places=5)

class Habitacion(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, unique=True)
    piso = models.IntegerField()

class TipoDispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    image = models.ImageField(upload_to="assets/tipo_dispositivos")

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    intensidad = models.IntegerField(default=255)
    pin = models.IntegerField(default=1)
    color = models.CharField(max_length=13, null=True)
    tipo = models.ForeignKey(TipoDispositivo, on_delete=models.PROTECT)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

class MedidasHabitacion(models.Model):
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    calidad_aire = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_hora = models.DateTimeField()

class EnergiaDispositivo(models.Model):
    fecha = models.DateField()
    energia = models.DecimalField(max_digits=5, decimal_places=2)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

class ProgramacionDispositivo(models.Model):
    inicio = models.TimeField()
    fin = models.TimeField()
    estado = models.BooleanField(default=True)
    intensidad = models.IntegerField(default=100)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)