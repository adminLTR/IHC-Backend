# Generated by Django 5.1.2 on 2024-10-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_habitacion_casa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='latitud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casa',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
