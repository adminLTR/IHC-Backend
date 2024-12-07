from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Casa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    longitud = models.FloatField(null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} house"
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"

class Habitacion(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    piso = models.PositiveIntegerField()
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.casa}({self.piso}) - {self.nombre}"

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

class TipoDispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    image = models.ImageField(upload_to="assets/tipo_dispositivos")

    def admin_image(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=self.image.url,
            width=30,
            height=30,
        ))
    admin_image.short_description = 'Image'
    admin_image.allow_tags = True

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de Dispositivo"
        verbose_name_plural = "Tipos de Dispositivos"


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    intensidad = models.PositiveIntegerField(default=100)
    pin = models.PositiveIntegerField(default=1, null=True)
    color = models.CharField(max_length=13, null=True)
    tipo = models.ForeignKey(TipoDispositivo, on_delete=models.PROTECT)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    volumen = models.FloatField(default=0, null=True)
    velocidad = models.PositiveSmallIntegerField(default=0, null=True)
    angulo = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.nombre} / {self.habitacion}"

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"

class MedidasHabitacion(models.Model):
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=5, decimal_places=2)
    calidad_aire = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Medida de Habitacion"
        verbose_name_plural = "Medidas de Habitaciones"

class EnergiaDispositivo(models.Model):
    fecha = models.DateField()
    energia = models.DecimalField(max_digits=5, decimal_places=2)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Energía de "
        verbose_name_plural = "Energía de dispositivos"

class ProgramacionDispositivo(models.Model):
    inicio = models.TimeField()
    fin = models.TimeField()
    estado = models.BooleanField(default=True)
    intensidad = models.IntegerField(default=100)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Programación de Dispositivo"
        verbose_name_plural = "Programación de Dispositivos"