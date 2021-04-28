from django import forms
from .models import *

'''class AnadirProductoForm(forms.Form):
    precio = forms.IntegerField(label="Precio", max_length=100)
    nombre = forms.CharField(label="Nombre", max_length=100)
    descripcion = forms.CharField(label="Descripción", max_length=100)
    categoria = forms.CharField(label="Categoria", max_length=100)
    relacion n-m

class AnadirPedidoForm(forms.Form):
    fecha = forms.CharField(label="Fecha", max_length=100)
    precioTotal = forms.IntegerField(label="Precio Total")
    cliente = forms.CharField(label="Cliente", max_length=100)'''
#clase formulario para los productos, cargamos todos los campos de dicho modelo
class ProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
#clase formulario para los pedidos, cargamos todos los campos de dicho modelo
class PedidoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'