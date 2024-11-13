import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Casa, Habitacion, TipoDispositivo, Dispositivo, MedidasHabitacion, EnergiaDispositivo, ProgramacionDispositivo
from faker import Faker
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        self.clean_data()

        self.stdout.write("Creating new data...")
        fake = Faker()

        # Create Users and Casa
        self.create_users_and_casas(fake, 10)

        # Create Habitaciones
        self.create_habitaciones(fake, 40)

        # Create Tipos de Dispositivo
        self.create_tipos_dispositivo(fake, 5)

        # Create Dispositivos
        self.create_dispositivos(fake, 30)

        # Create MedidasHabitacion
        self.create_medidas_habitacion(fake, 50)

        # Create EnergiaDispositivo
        self.create_energia_dispositivo(fake, 50)


    def clean_data(self):
        """ Remove old data from the database """
        ProgramacionDispositivo.objects.all().delete()
        EnergiaDispositivo.objects.all().delete()
        MedidasHabitacion.objects.all().delete()
        Dispositivo.objects.all().delete()
        TipoDispositivo.objects.all().delete()
        Habitacion.objects.all().delete()
        Casa.objects.all().delete()
        User.objects.all().delete()

    def create_users_and_casas(self, fake, count):
        for _ in range(count):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password'
            )
            Casa.objects.create(
                usuario=user,
                longitud=fake.longitude(),
                latitud=fake.latitude(),
            )
        User.objects.create_superuser('admin', '', '1234')

    def create_habitaciones(self, fake, count):
        casas = Casa.objects.all()
        habitaciones = ("cocina", "comedor", "sala", "dormitorio principal", "dormitorio secundario", "baño", "cuarto de lavado", "garaje", "estudio", "terraza")
        for _ in range(count):
            Habitacion.objects.create(
                nombre=random.choice(habitaciones),
                piso=random.randint(1, 3),
                casa=random.choice(casas)
            )

    def create_tipos_dispositivo(self, fake, count):
        tipos = ["luces", "camara", "microfono", "electrodomestico"]
        for tipo in tipos:
            TipoDispositivo.objects.create(
                nombre=tipo,
                descripcion=fake.sentence(),
                image="/assets/tipo_dispositivos/"+tipo+".png"
            )

    def create_dispositivos(self, fake, count):
        habitaciones = Habitacion.objects.all()
        tipos_dispositivo = TipoDispositivo.objects.all()
        for _ in range(count):
            habitacion = random.choice(habitaciones)
            tipo_dispositivo = random.choice(tipos_dispositivo)
            Dispositivo.objects.create(
                nombre=fake.word() if tipo_dispositivo.nombre=='electrodomestico' else tipo_dispositivo.nombre,
                pin=random.randint(1, 40),
                color=hex(random.randint(0, int("ffffff", 16))).strip('0x'),
                tipo=tipo_dispositivo,
                habitacion=habitacion
            )

    def create_medidas_habitacion(self, fake, count):
        habitaciones = Habitacion.objects.all()
        for habitacion in habitaciones:
            for _ in range(100):
                MedidasHabitacion.objects.create(
                    temperatura=round(random.uniform(15.0, 30.0), 2),
                    humedad=round(random.uniform(30.0, 70.0), 2),
                    calidad_aire=round(random.uniform(0.0, 1.0), 2),
                    habitacion=habitacion,
                    fecha_hora=Command.fecha_hora_aleatoria('2024-01-01 00:00:00', '2024-12-31 23:59:59')
                )

    def create_energia_dispositivo(self, fake, count):
        dispositivos = Dispositivo.objects.all()
        for dispositivo in dispositivos:
            EnergiaDispositivo.objects.create(
                fecha=fake.date(),
                energia=round(random.uniform(0.0, 100.0), 2),
                dispositivo=dispositivo
            )

    def fecha_hora_aleatoria(inicio, fin):
        """
        Genera una fecha y hora aleatoria entre dos fechas.
        
        :param inicio: Fecha inicial en formato 'YYYY-MM-DD HH:MM:SS'
        :param fin: Fecha final en formato 'YYYY-MM-DD HH:MM:SS'
        :return: Fecha y hora aleatoria en formato 'YYYY-MM-DD HH:MM:SS'
        """
        fecha_inicio = datetime.strptime(inicio, '%Y-%m-%d %H:%M:%S')
        fecha_fin = datetime.strptime(fin, '%Y-%m-%d %H:%M:%S')
        
        diferencia = fecha_fin - fecha_inicio
        segundos_aleatorios = random.randint(0, int(diferencia.total_seconds()))
        
        fecha_aleatoria = fecha_inicio + timedelta(seconds=segundos_aleatorios)
        return fecha_aleatoria
