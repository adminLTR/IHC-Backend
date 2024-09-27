from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Casa)
admin.site.register(Habitacion)
admin.site.register(TipoDispositivo)
admin.site.register(Dispositivo)
admin.site.register(MedidasHabitacion)
admin.site.register(EnergiaDispositivo)
admin.site.register(ProgramacionDispositivo)