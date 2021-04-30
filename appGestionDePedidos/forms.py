from django import forms
from .models import *

#Clase formulario para los productos, cargamos todos los campos de dicho modelo
class ProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

#Clase formulario para los pedidos, cargamos todos los campos de dicho modelo, excepto el listado de productos (se añadirán en otro formulario)
class PedidoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['productos']

#Clase formulario para la relación pedido-producto, cargamos todos los campos de dicho modelo
class PedidoProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Compone
        fields = '__all__'

#Clase formulario para la relación componente-producto, cargamos todos los campos de dicho modelo
class ComponenteProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Consta
        fields = '__all__'
        
