from django.urls import path
from . import views
from appGestionDePedidos.views import *

urlpatterns = [
    #URL para la pag. principal donde se visualizará el listado de productos y pedidos
    path('', ProductoPedidoListView.as_view(), name = 'pagPrincipal'),
    #URL para la visualización de cada atributo de un producto concreto
    path('detalleProducto/<int:pk>/', ProductoDetailView.as_view(), name = 'detalleProducto'),
    #URL para la visualización de cada atributo de un pedido concreto
    path('detallePedido/<int:pk>/', PedidoDetailView.as_view(), name = 'detallePedido'),
    #URL para acceder al formulario en el cual se podrá añadir un producto nuevo
    path('anyadirProducto/', AnyadirProductoForm.as_view(), name="anyadirProducto"),
]