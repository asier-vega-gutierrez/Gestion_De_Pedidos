from django.shortcuts import render, redirect
from .models import Cliente, Componente, Producto, Pedido
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django import forms
from django.views import View

# Create your views here.

def pagPrincipal(request):
    context = {}
    return render(request, "pagPrincipal.html", context)

class ProductoListView(ListView):

        model = Producto
        template_name = 'ListaProducto.html'
        context_object_name = 'lista_productos'

        '''def get_context_data(self, **kwargs):
                context = super(ProductoListView, self).get_context_data(**kwargs)
                return context'''
        
       

class ProductoDetailView(DetailView):

        model = Producto
        template_name = 'DetalleProducto.html'
        context_object_name = 'Detalle_producto'

        '''def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                #context['lista_productos'] = 
                return context'''


class PedidoListView(ListView):

        model = Pedido
        template_name = 'ListaPedido.html'
        context_object_name = 'lista_pedidos'

        '''def get_context_data(self, **kwargs):
                context = super(PedidoListView, self).get_context_data(**kwargs)
                
                return context'''

'''class PedidoDetailView(DetailView):

        model = Pedido
        #template_name = 
    
class ClienteListView(ListView):

        model = Cliente
        #template_name = 

class ComponenteListView(ListView):

        model = Componente
        #template_name = 
'''

class AnadirProductoForm(View):

        def get(self, request, *args, **kwargs):
                form = AnadirProductoForm()
                context = {'form': form}
                return render(request, 'AnadirProducto.html', context)

        def post(self, request, *args, **kwargs):
                form = AnadirProductoForm(request.POST)
                if form.is_valid():
                        producto = Producto()
                        producto.precio = form.cleaned_data['precio']
                        producto.nombre = form.cleaned_data['nombre']
                        producto.descripcion = form.cleaned_data['descripcion']
                        producto.categoria = form.cleaned_data['categoria']
                        producto.save()
                        # Volvemos a la lista de departamentos
                        return redirect('producto')

                return render(request, 'AnadirProducto.html', {'form': form})