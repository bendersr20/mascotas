from django.db import models

# Create your models here.

class Perro(models.Model):
    a_id = models.IntegerField(default=1)
    nombre = models.TextField(max_length=20)
    tamaño = models.TextField(max_length=10)
    peso = models.TextField(max_length=5)
    color = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=50)
    fecharescate = models.DateField('fecha rescate')
    estado = models.TextField(max_length=10)

    def listar(self):
        cadena = "{0},{1},{2},{3},{4},{5},{6},{7}"
        return self.a_id, self.nombre, self.tamaño, self.peso, self.color, self.descripcion, self.fecharescate, self.estado

    def __str__(self):
        return self.listar()




