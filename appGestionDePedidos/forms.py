from django import forms
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'groups',
        ] 

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

#Clase formulario para los clientes, cargamos todos los campos de dicho modelo
class ClienteAnyadirForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

#Clase formulario para los componentes, cargamos todos los campos de dicho modelo
class ComponenteAnyadirForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'

#Clase formulario para enviar correos al correo de contacto
class EnviarMail(forms.Form):
    Nombre = forms.CharField(max_length = 25)
    Apellidos = forms.CharField(max_length = 50)
    Email = forms.EmailField()
    Mensaje = forms.CharField(widget = forms.Textarea)