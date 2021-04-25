from django.urls import path
from . import views
from appGestionDePedidos.views import *

urlpatterns = [
    path('', views.pagPrincipal, name = 'pagPrincipal'),
    path('ListaProducto/', ProductoListView.as_view(), name = 'ListaProducto'),
    path('DetalleProducto/<str:nombre_producto>', ProductoDetailView.as_view(), name = 'DetalleProducto'),
]