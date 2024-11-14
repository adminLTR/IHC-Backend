from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'casas', CasaViewSet)
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'tipos-dispositivos', TipoDispositivoViewSet)
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'medidas-habitaciones', MedidasHabitacionViewSet)
router.register(r'energia-dispositivos', EnergiaDispositivoViewSet)
router.register(r'programaciones-dispositivos', ProgramacionDispositivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dispositivos/all', home_view, name='home_view'),
    path('habitaciones/medidas', post_medida_habitacion, name='post_medidas')
]