from django.urls import path, include 
from . import views
from appGestionDePedidos.views import *

urlpatterns = [
    #URL de Django para crear los forms Login y Logout
    path('accounts/', include('django.contrib.auth.urls')),

    #URL para la pag. principal donde se visualizará todos los listados
    path('', ListadosListView.as_view(), name = 'pagPrincipal'),

    #URLS PARA DETALLES
    #URL para la visualización de cada atributo de un producto concreto
    path('detalleProducto/<int:pk>/', ProductoDetailView.as_view(), name = 'detalleProducto'),
    #URL para la visualización de cada atributo de un pedido concreto
    path('detallePedido/<int:pk>/', PedidoDetailView.as_view(), name = 'detallePedido'),
    #URL para la visualización de cada atributo de un cliente concreto
    path('detalleCliente/<int:pk>/', ClienteDetailView.as_view(), name = 'detalleCliente'),
    #URL para la visualización de cada atributo de un componente concreto
    path('detalleComponente/<int:pk>/', ComponenteDetailView.as_view(), name = 'detalleComponente'),

    #URLS PARA AÑADIR
    #URL para acceder al formulario en el cual se podrá añadir un producto nuevo
    path('anyadirProducto/', views.AnyadirProductoForm.as_view(), name="anyadirProducto"),
    #URL para acceder al formulario en el cual se podrá añadir un pedido nuevo
    path('anyadirPedido/', views.AnyadirPedidoForm.as_view(), name="anyadirPedido"),
    #URL para acceder al formulario en el cual se podrá asignar un producto existente a un pedido existente
    path('anyadirPedidoProducto/', views.AnyadirPedidoProductoForm.as_view(), name="anyadirPedidoProducto"),
    #URL para acceder al formulario en el cual se podrá asignar un producto existente a un componente existente
    path('anyadirComponenteProducto/', views.AnyadirComponenteProductoForm.as_view(), name="anyadirComponenteProducto"),
    #URL para acceder al formulario en el cual se podrá añadir un cliente nuevo
    path('anyadirCliente/', views.AnyadirClienteForm.as_view(), name="anyadirCliente"),
    #URL para acceder al formulario en el cual se podrá añadir un componente nuevo
    path('anyadirComponente/', views.AnyadirComponenteForm.as_view(), name="anyadirComponente"),

    #URLS PARA ELIMINAR
    #URL para acceder al formulario en el cual se podrá eliminar un producto ya existente
    path('eliminarProducto/<int:pk>/', EliminarProducto.as_view(), name = 'eliminarProducto'),
    #URL para acceder al formulario en el cual se podrá eliminar un pedido ya existente
    path('eliminarPedido/<int:pk>/', EliminarPedido.as_view(), name = 'eliminarPedido'),
    #URL para acceder al formulario en el cual se podrá eliminar un cliente ya existente
    path('eliminarCliente/<int:pk>/', EliminarCliente.as_view(), name = 'eliminarCliente'),
    #URL para acceder al formulario en el cual se podrá eliminar un componente ya existente
    path('eliminarComponente/<int:pk>/', EliminarComponente.as_view(), name = 'eliminarComponente'),

    #URLS PARA MODIFICAR
    #URL para acceder al formulario en el cual se podrá modificar un pedido ya existente
    path('modificarPedido/<int:pk>/', ModificarPedido.as_view(), name = 'modificarPedido'),
    #URL para acceder al formulario en el cual se podrá modificar un producto ya existente
    path('modificarProducto/<int:pk>/', ModificarProducto.as_view(), name = 'modificarProducto'),
    #URL para acceder al formulario en el cual se podrá modificar un cliente ya existente
    path('modificarCliente/<int:pk>/', ModificarCliente.as_view(), name = 'modificarCliente'),
    #URL para acceder al formulario en el cual se podrá modificar un componente ya existente
    path('modificarComponente/<int:pk>/', ModificarComponente.as_view(), name = 'modificarComponente'),
]