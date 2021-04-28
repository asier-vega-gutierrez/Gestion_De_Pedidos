from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, ListView, UpdateView
from django.views import View
from django import forms
from django.urls import reverse_lazy

from .forms import *
from .models import *

#Vista basada en clase que nos coge un listado de todos los productos para poder trabajar con ellos en el html
class ProductoPedidoListView(ListView):
        model = Producto
        template_name = 'pagPrincipal.html'
        context_object_name = 'lista_productos'

        #Añadimos a la vista un listado de todos los pedidos existentes mediante la función get_context_data
        def get_context_data(self, **kwargs):
                context = super(ProductoPedidoListView, self).get_context_data(**kwargs)
                context['lista_pedidos'] = Pedido.objects.all()
                return context

#Vista basada en clase que nos coge todos los atributos de un producto concreto para poder trabajar con ellos en el html
class ProductoDetailView(DetailView):
        model = Producto
        template_name = 'detalleProducto.html'
        context_object_name = 'detalle_producto'

#Vista basada en clase que nos coge todos los atributos de un pedido concreto para poder trabajar con ellos en el html
class PedidoDetailView(DetailView):
        model = Pedido
        template_name = 'detallePedido.html'
        context_object_name = 'detalle_pedido'


class AnyadirProductoForm(View):
        def get(self, request, *args, **kwargs):
                form = ProductoAnyadirForm()
                context = {'form': form}
                return render(request, 'anyadirProducto.html', context)

        def post(self, request, *args, **kwargs):
                form = ProductoAnyadirForm(request.POST)
                if form.is_valid():
                        producto = Producto()
                        producto.nombre = form.cleaned_data['nombre']
                        producto.precio = form.cleaned_data['precio']
                        producto.categoria = form.cleaned_data['categoria']
                        producto.descripcion = form.cleaned_data['descripcion']
                        producto.save()
                        # Volvemos a la lista de departamentos
                        return redirect('pagPrincipal')
                return render(request, 'anyadirProducto.html', {'form': form})

#vista basada en clases de tipo deleteView que nos vale para eliminar un producto
class EliminarProducto(DeleteView):
        model = Producto
        template_name = 'eliminarProducto.html'
        success_url = reverse_lazy('pagPrincipal')


class AnyadirPedidoForm(View):
        def get(self, request, *args, **kwargs):
                form = PedidoAnyadirForm()
                context = {'form': form}
                return render(request, 'anyadirPedido.html', context)

        def post(self, request, *args, **kwargs):
                form = PedidoAnyadirForm(request.POST)
                if form.is_valid():
                        pedido = Pedido()
                        pedido.fecha = form.DateField['fecha']
                        pedido.precioTotal = form.cleaned_data['nombre']
                        pedido.cliente = form.cleaned_data['cliente']
                        pedido.productos = form.cleaned_data['productos']
                        pedido.save()
                        # Volvemos a la lista de departamentos
                        return redirect('pagPrincipal')
                return render(request, 'anyadirPedido.html', {'form': form})

#vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos 
class ModificarPedido(UpdateView):
        model = Pedido
        template_name = 'modificarPedido.html'
        success_url = reverse_lazy('pagPrincipal')

        '''def get_context_data(self, **kwargs):
                context = super(ModificarPedido, self).get_context_data(**kwargs)
                context['cantidad'] = Compone.cantidad
                return context'''

        fields = {
                "fecha",
                "precioTotal",
                "cliente",
                #"productos",
                #"cantidad"
                #se necesita el atributo cantidad para modificar los prodcutos, si no da error
        }
                