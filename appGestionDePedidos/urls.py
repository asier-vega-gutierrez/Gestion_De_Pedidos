from django.urls import path
from . import views
from appGestionDePedidos.views import *

urlpatterns = [
    #URL para la pag. principal donde se visualizará el listado de productos y pedidos
    path('', ProductoPedidoListView.as_view(), name = 'pagPrincipal'),

    #URLS PARA DETALLES
    #URL para la visualización de cada atributo de un producto concreto
    path('detalleProducto/<int:pk>/', ProductoDetailView.as_view(), name = 'detalleProducto'),
    #URL para la visualización de cada atributo de un pedido concreto
    path('detallePedido/<int:pk>/', PedidoDetailView.as_view(), name = 'detallePedido'),

    #URLS PARA AÑADIR
    #URL para acceder al formulario en el cual se podrá añadir un producto nuevo
    path('anyadirProducto/', views.AnyadirProductoForm.as_view(), name="anyadirProducto"),
    #URL para acceder al formulario en el cual se podrá añadir un producto nuevo
    path('anyadirPedido/', views.AnyadirPedidoForm.as_view(), name="anyadirPedido"),

    path('anyadirPedidoProducto/', views.AnyadirPedidoProductoForm.as_view(), name="anyadirPedidoProducto"),
    
    path('anyadirComponenteProducto/', views.AnyadirComponenteProductoForm.as_view(), name="anyadirComponenteProducto"),

    #URLS PARA ELIMINAR
    #URL para acceder al formulario en el cual se podrá eliminar un producto ya existente
    path('eliminarProducto/<int:pk>/', EliminarProducto.as_view(), name = 'eliminarProducto'),
    
    #URLS PARA MODIFICAR
    #URL para acceder al formulario en el cual se podrá modificar un pedido ya existente
     path('modificarPedido/<int:pk>/', ModificarPedido.as_view(), name = 'modificarPedido'),
    
]