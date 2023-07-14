from django.db import models

# Create your models here.


class Jugadores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30,null=False)
    apellido = models.CharField(max_length=30,null=False)
    posicion = models.CharField(max_length=2,null=False)
    fecha_deb = models.DateField(null=False)
    fecha_ret = models.DateField(null=False)
    class Meta:
        db_table = 'jugadores' 
