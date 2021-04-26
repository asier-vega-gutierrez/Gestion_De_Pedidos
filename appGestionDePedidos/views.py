from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django import forms
from django.views import View

class ProductoPedidoListView(ListView):
        model = Producto
        template_name = 'pagPrincipal.html'
        context_object_name = 'lista_productos'

        def get_context_data(self, **kwargs):
                context = super(ProductoPedidoListView, self).get_context_data(**kwargs)
                context['lista_pedidos'] = Pedido.objects.all()
                return context

class ProductoDetailView(DetailView):
        model = Producto
        template_name = 'detalleProducto.html'
        context_object_name = 'detalle_producto'

        def get_context_data(self, **kwargs):
                context = super(ProductoDetailView, self).get_context_data(**kwargs)
                context['lista_pedidos_productos'] = Compone.objects.filter(producto=self.object.id)
                return context

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

class AnyadirProductoForm(View):

        def get(self, request, *args, **kwargs):
                form = AnadirProductoForm()
                context = {'form': form}
                return render(request, 'anyadirProducto.html', context)

        def post(self, request, *args, **kwargs):
                form = AnyadirProductoForm(request.POST)
                if form.is_valid():
                        producto = Producto()
                        producto.precio = form.cleaned_data['precio']
                        producto.nombre = form.cleaned_data['nombre']
                        producto.descripcion = form.cleaned_data['descripcion']
                        producto.categoria = form.cleaned_data['categoria']
                        producto.save()
                        # Volvemos a la lista de departamentos
                        return redirect('producto')

                return render(request, 'anyadirProducto.html', {'form': form})