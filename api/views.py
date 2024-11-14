from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from rest_framework import viewsets, status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        user = User.objects.first()
        casa = Casa.objects.get(usuario=user)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(casa=casa)  # Asignar la primera categoría
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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


def home_view(request, user_id):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    # user = User.objects.get(id=user_id)
    user = User.objects.first()
    if not user:
        return JsonResponse({'error': 'User not found'}, status=400)
    
    casa = Casa.objects.get(usuario_id=user.pk)
    habitaciones = Habitacion.objects.filter(casa_id=casa.pk)


    data = {
        'longitud': casa.longitud,
        'latitud': casa.latitud,
        'habitaciones': [ # arreglo de habitaciones por cada casa
            {
                'id': habitacion.id,
                'nombre' : habitacion.nombre,
                'piso': habitacion.piso,
                'dispositivos': [
                    {
                        'id' : dispositivo.id,
                        'nombre': dispositivo.nombre,
                        'imagen' : dispositivo.tipo.image.url
                    }
                    for dispositivo in Dispositivo.objects.filter(habitacion_id = habitacion.id)
                ]
            }
            for habitacion in habitaciones
        ]
    }
    return JsonResponse(data)

@csrf_exempt
def post_medida_habitacion(request, habitacion_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)

        temperatura = data.get('temperatura')
        humedad = data.get('humedad')
        calidad_aire = data.get('calidad_aire')

        if not temperatura or not humedad or not calidad_aire:
            return JsonResponse({'error': 'Campos faltantes en la solicitud'}, status=400)
        
        user = User.objects.first()
        habitacion = Habitacion.objects.get(user=user)

        medidas = MedidasHabitacion.objects.create(temperatura=temperatura, humedad=humedad, calidad_aire=calidad_aire, habitacion=habitacion)
        
        return JsonResponse({
            'status' : 'success'
        }, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Solicitud malformada. Debe ser JSON válido'}, status=400)