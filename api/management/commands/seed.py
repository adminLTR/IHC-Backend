import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Casa, Habitacion, TipoDispositivo, Dispositivo, MedidasHabitacion, EnergiaDispositivo, ProgramacionDispositivo
from faker import Faker

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

        # # Create Dispositivos
        # self.create_dispositivos(fake, 30)

        # # Create MedidasHabitacion
        # self.create_medidas_habitacion(fake, 50)

        # # Create EnergiaDispositivo
        # self.create_energia_dispositivo(fake, 50)

        # # Create ProgramacionDispositivo
        # self.create_programacion_dispositivo(fake, 50)

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
                nombre=tipos,
                descripcion=fake.sentence(),
                image="/media/assets/tipo_dispositivos/"+tipo
            )

    def create_dispositivos(self, fake, count):
        habitaciones = Habitacion.objects.all()
        tipos_dispositivo = TipoDispositivo.objects.all()
        for _ in range(count):
            habitacion = random.choice(habitaciones)
            tipo_dispositivo = random.choice(tipos_dispositivo)
            Dispositivo.objects.create(
                nombre=fake.word(),
                estado=random.choice([True, False]),
                intensidad=random.randint(0, 100),
                pin=random.randint(1, 40),
                color=fake.color_name(),
                tipo=tipo_dispositivo,
                habitacion=habitacion
            )

    def create_medidas_habitacion(self, fake, count):
        habitaciones = Habitacion.objects.all()
        for _ in range(count):
            habitacion = random.choice(habitaciones)
            MedidasHabitacion.objects.create(
                temperatura=round(random.uniform(15.0, 30.0), 2),
                humedad=round(random.uniform(30.0, 70.0), 2),
                calidad_aire=round(random.uniform(0.0, 1.0), 2),
                habitacion=habitacion
            )

    def create_energia_dispositivo(self, fake, count):
        dispositivos = Dispositivo.objects.all()
        for _ in range(count):
            dispositivo = random.choice(dispositivos)
            EnergiaDispositivo.objects.create(
                fecha=fake.date(),
                energia=round(random.uniform(0.0, 100.0), 2),
                dispositivo=dispositivo
            )

    def create_programacion_dispositivo(self, fake, count):
        dispositivos = Dispositivo.objects.all()
        for _ in range(count):
            dispositivo = random.choice(dispositivos)
            ProgramacionDispositivo.objects.create(
                inicio=fake.time(),
                fin=fake.time(),
                estado=random.choice([True, False]),
                intensidad=random.randint(0, 100),
                dispositivo=dispositivo
            )
