from django.contrib import admin
from .models import *

class CasaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Casa._meta.fields]

class HabitacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Habitacion._meta.fields]
    list_filter = ('casa', 'piso')

class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_image', 'nombre', 'descripcion')

class DispositivoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dispositivo._meta.fields]

class MedidasHabitacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MedidasHabitacion._meta.fields]

# Register your models here.
admin.site.register(Casa, CasaAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(TipoDispositivo, TipoDispositivoAdmin)
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(MedidasHabitacion, MedidasHabitacionAdmin)
admin.site.register(EnergiaDispositivo)
admin.site.register(ProgramacionDispositivo)