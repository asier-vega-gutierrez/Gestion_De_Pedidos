from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagPrincipal, name = 'pagPrincipal'),
    path('DetalleProducto/<str:nombre_producto>', views.ProductoDetailView.as_view(), name = 'DetalleProducto')
]