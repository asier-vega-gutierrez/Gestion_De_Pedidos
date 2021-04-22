from django.shortcuts import render
from .models import Cliente, Componente, Producto, Pedido
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

def index(request):
    context = {}
    return render(request, "base.html", context)

#class ProductoListView(ListView):

#class ProductoDetailView(DetailView):

#class PedidoListView(ListView):

#class PedidoDetailView(DetailView):