from django.contrib import admin
from .models import Cliente, Pedido, Producto, Componente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Componente)