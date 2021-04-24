from django.shortcuts import render
from .models import Cliente, Componente, Producto, Pedido
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

def pagPrincipal(request):
    context = {}
    return render(request, "pagPrincipal.html", context)

class ProductoListView(ListView):

        model = Producto
        template_name = 'ListaProductos.html'
        context_object_name = 'lista_productos'

        def get_context_data(self, **kwargs):
                context = super(ProductoListView, self).get_context_data(**kwargs)
                context['Titulo_Pagina'] = 'Listado de productos'
                return context

class ProductoDetailView(DetailView):

        model = Producto
        #template_name = 

class PedidoListView(ListView):

        model = Pedido
        #template_name = 

class PedidoDetailView(DetailView):

        model = Pedido
        #template_name = 
    
class ClienteListView(ListView):

        model = Cliente
        #template_name = 

class ComponenteListView(ListView):

        model = Componente
        #template_name = 