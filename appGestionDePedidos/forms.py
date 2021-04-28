from django import forms
from .models import *

#clase formulario para los productos, cargamos todos los campos de dicho modelo
class ProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['componentes']

#clase formulario para los pedidos, cargamos todos los campos de dicho modelo
class PedidoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Compone
        fields = '__all__'

class ComponenteProductoAnyadirForm(forms.ModelForm):
    class Meta:
        model = Consta
        fields = '__all__'
        
