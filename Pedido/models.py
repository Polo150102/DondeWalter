from django.db import models

# Create your models here.

class Tipo_comida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=False)
    class Meta:
        db_table = 'tipo_comida' 

class Plato_extra(models.Model):
    id_extra = models.AutoField(primary_key=True)
    nombre_extra = models.TextField(blank=False)
    precio_extra = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    imagen_extra = models.TextField(blank=False)

    class Meta:
        db_table = 'plato_extra'  

class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre_plato = models.TextField(blank=False)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    imagen = models.TextField(blank=False)
    id_tipo_carta = models.ForeignKey(Tipo_comida, on_delete=models.CASCADE, db_column='id_tipo_carta')

    class Meta:
        db_table = 'menu'
