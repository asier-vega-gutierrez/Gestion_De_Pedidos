
from django.db import models


class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    nombreEmpresa = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre

class Componente(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    precio = models.IntegerField()
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    componente = models.ManyToManyField(Componente) #esto nos crea la tabla intermedia de la n-m invisible producto-componente

    def __str__(self):
        return self.nombre
        
class Pedido(models.Model):
    fecha = models.CharField(max_length=50)
    precioTotal = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #para la recacion 1-n con cliente
    producto = models.ManyToManyField(Producto) #esto nos crea la tabla intermedia de la n-m invisible de pedido-producto

    def __str__(self):
        return self.fecha




