from django.urls import path
from . import views
from appGestionDePedidos.views import *

urlpatterns = [
    path('', views.pagPrincipal, name = 'pagPrincipal'),
    path('ListaProducto/', ProductoListView.as_view(), name = 'ListaProducto'),
    path('DetalleProducto/<int:pk>', ProductoDetailView.as_view(), name = 'DetalleProducto'),
    path('ListaPedidos/', PedidoListView.as_view(), name = 'ListaPedido'),
    path('AnadirProducto/', AnadirProductoForm.as_view(), name="AnadirProducto"),
]