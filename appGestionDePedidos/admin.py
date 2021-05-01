from django.contrib import admin
from .models import *

#Registramos nuestros modelos para ejecutar los comandos 'makemigrations' y 'migrate'
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(Consta)
admin.site.register(Compone)