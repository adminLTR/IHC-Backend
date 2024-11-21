from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ['usuario', 'longitud', 'latitud']


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['id', 'nombre', 'piso']


class TipoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDispositivo
        fields = ['id', 'nombre', 'descripcion', 'image']


class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'


class MedidasHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedidasHabitacion
        fields = ['temperatura', 'humedad', 'calidad_aire', 'fecha_hora']


class EnergiaDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergiaDispositivo
        fields = ['fecha', 'energia', 'dispositivo']


class ProgramacionDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionDispositivo
        fields = ['inicio', 'fin', 'estado', 'intensidad', 'dispositivo']