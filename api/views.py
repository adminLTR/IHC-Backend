from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CasaViewSet(viewsets.ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


class TipoDispositivoViewSet(viewsets.ModelViewSet):
    queryset = TipoDispositivo.objects.all()
    serializer_class = TipoDispositivoSerializer


class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer


class MedidasHabitacionViewSet(viewsets.ModelViewSet):
    queryset = MedidasHabitacion.objects.all()
    serializer_class = MedidasHabitacionSerializer


class EnergiaDispositivoViewSet(viewsets.ModelViewSet):
    queryset = EnergiaDispositivo.objects.all()
    serializer_class = EnergiaDispositivoSerializer


class ProgramacionDispositivoViewSet(viewsets.ModelViewSet):
    queryset = ProgramacionDispositivo.objects.all()
    serializer_class = ProgramacionDispositivoSerializer