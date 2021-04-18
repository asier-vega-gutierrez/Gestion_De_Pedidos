from django.db import models


class Cliente(models.Model):
    id_cliente = models.CharField(max_length=5)
    cif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=9)
    nombreEmpresa = models.CharField(max_length=50)
    email = models.EmailField(max_legth=50)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    id_pedido = models.CharField(max_length=5)
    fecha = models.CharField(max_length=50)
    precioTotal = models.IntegerField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #para la recacion 1-n con cliente
    producto = models.ManyToManyField(Producto) #esto nos crea la tabla intermedia de la n-m invisible de pedido-producto

class Producto(models.Model):
    id_producto = models.CharField(max_length=5)
    precio = models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    componente = models.ManyToManyField(Componente) #esto nos crea la tabla intermedia de la n-m invisible producto-componente

    def __str__(self):
        return self.nombre

class Componente(models.Model):
    id_componente= models.CharField(max_length=5)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
