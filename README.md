# BACKEND

Esta carpeta contiene el backend del proyecto, desarrollado en Django y otras tecnologías. A continuación, encontrarás las instrucciones necesarias para levantar el proyecto localmente, instalar las dependencias, y algunos recursos adicionales.


## Tecnologías Utilizadas

Para este proyecto, las principales dependencias son:

- **Python**: Lenguaje principal del proyecto de backend. Puedes encontrar la documentación oficial [aquí](https://www.python.org/)
- **Django**: Framework de desarrollo web. Puedes encontrar la documentación oficial [aquí](https://www.djangoproject.com/)
- **Django REST Framework**: Utilizado para crear APIs RESTful. Puedes encontrar la documentación oficial [aquí](https://www.django-rest-framework.org/)
- **Django CORS Headers**: Para gestionar las políticas de intercambio de recursos entre orígenes (CORS). Puedes encontrar la documentación oficial [aquí](https://pypi.org/project/django-cors-headers/)
- **Pillow**: Biblioteca de imágenes en Python. Puedes encontrar la documentación oficial [aquí](https://pillow.readthedocs.io/en/stable/)
- **Django Jazzmin**: Biblioteca de personalización de admin panel basado en AdminLTE y Bootstrap. Puedes encontrar la documentación oficial [aquí](https://django-jazzmin.readthedocs.io/)

## Requisitos previos

Como es de esperarse, primero debemos instalar el lenguaje en el que está desarrollado el proyecto. Puedes instalar la última versión de Python [aquí](https://www.python.org/downloads/).

[Aquí](https://www.youtube.com/watch?v=i6j8jT_OdEU) tienes un video de instalación por si te queda alguna duda.

## Instalación del proyecto

Si tienes ya instalada la última versión de Python, abre una consola y dirigete a esta carpeta mediante la linea de comandos, o abrela directamente en esta misma carpeta **(IHC-G5/desarrollo/backend)**.

Posteriormente, debes crear un entorno virtual, pero para eso, debes instalar una dependencia de python 'virtualenv'. Así que en esa misma consola, escribe el comando **pip install virtualenv**

Luego, crea el entorno virtual, así que en la misma consola, escribe el comando **virtualenv env**, esto creará una nueva carpeta (env), la cual será el entorno virtual del proyecto, en este se instalarán todas nuestras dependencias.

Pero antes de instalar las dependencias, debes activar tu entorno virtual. asi que dentro de esa misma carpeta en la consola previamente abierta coloca el siguiente comando: **./env/Scripts/activate**, esto debería activar tu entorno virtual. Es importante que cada vez que requieras trabajar con el proyecto, tengas el entorno virtual prendido, por lo que siempre debes correr este comando cada vez que quieras levantarlo.

Por último, instalaremos todas las dependencias necesarias para nuestro proyecto, estas se encuentran en el archivo *requirements.txt*. Para instalar las dependencias, y con el entorno virtual encendido, corre el siguiente comando: **pip install -r requirements.txt**

## Levantamiento del proyecto

Para levantar el proyecto, debes tener todas las dependencias instaladas previamente. Además, debes tener el entorno virtual encendido, con el comando **./env/Scripts/activate**

Si no tienes ya previamente la base de datos instalada, debes correr las migraciones, solo lo harás una vez o cuando el *desarrollador backend* haga algún cambio grande, así que dentro de nuestra carpeta en la consola y con el entorno virtual encendido colocamos el siguiente comando: **python manage.py migrate**. Esto creará y/o modelará la base de datos la base de datos.

Si ya tienes la base de datos migrada, simplemente corre el comando **python manage.py runserver 0.0.0.0:8000**, esto creará un servidor para el backend que podrá intercambiar datos con el frontend


## Endpoints
### (GET) dispositivos/all 
Obtiene todos los dispositivos de todas las habitaciones de todas la casa del usuario con id=user_id

### (POST) habitaciones/medidas
Envia datos de las medidas de la habitacion con id=habitacion_id. Recibe temperatura, humedad y aire

### (POST) /habitaciones
