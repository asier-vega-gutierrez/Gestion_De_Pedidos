from django.db import models

#Creacion del objeto cliente con sus respectivos atributos.
class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    nombreEmpresa = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    #Funcion utilizada para mostrar el nombre del cliente en vez de la PK.
    def __str__(self):
        return self.nombre

#Creacion del objeto componente con sus respectivos atributos.
class Componente(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    
    #Funcion utilizada para mostrar el nombre del componente en vez de la PK.
    def __str__(self):
        return self.nombre
        
#Creacion del objeto producto con sus respectivos atributos.        
class Producto(models.Model):
    precio = models.IntegerField()
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    categoria = models.CharField(max_length=50)
    componentes = models.ManyToManyField(Componente, through = 'Consta') #esto nos crea la tabla intermedia de la n-m invisible producto-componente

    #Funcion utilizada para mostrar el nombre del producto en vez de la PK.
    def __str__(self):
        return self.nombre
        
#Creacion del objeto pedido con sus respectivos atributos.        
class Pedido(models.Model):
    fecha = models.DateField()
    precioTotal = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #para la recacion 1-n con cliente
    productos = models.ManyToManyField(Producto, through = 'Compone')#esto nos crea la tabla intermedia de la n-m invisible de pedido-producto
    
    #Funcion utilizada para mostrar la fecha del pedido en vez de la PK.
    def __str__(self):
        return str(self.fecha)

#Creacion de un objeto "consta" utilizado para hacer de enlace en la relacion n-m entre producto y componente.
class Consta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

#Creacion de un objeto "compone" utilizado para hacer de enlace en la relacion n-m entre producto y pedido, añadiendo un nuevo atributo, cantidad.
class Compone(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default='1')





