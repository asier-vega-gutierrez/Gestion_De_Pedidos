
from django.db import models


class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
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
    descripcion = models.TextField(max_length=50)
    categoria = models.CharField(max_length=50)
    componentes = models.ManyToManyField(Componente, through = 'Consta') #esto nos crea la tabla intermedia de la n-m invisible producto-componente

    def __str__(self):
        return self.nombre
        
class Pedido(models.Model):
    fecha = models.DateField()
    precioTotal = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #para la recacion 1-n con cliente
    productos = models.ManyToManyField(Producto, through = 'Compone')#esto nos crea la tabla intermedia de la n-m invisible de pedido-producto
    def __str__(self):
        return str(self.fecha)

class Consta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

class Compone(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()





