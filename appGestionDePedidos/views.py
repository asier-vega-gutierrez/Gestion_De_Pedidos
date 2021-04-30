from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from django.views import View
from django import forms
from django.urls import reverse_lazy

from .forms import *
from .models import *

#Vista basada en clases que nos coge un listado de todos los productos para poder trabajar con ellos en el html
class ListadosListView(ListView):
        model = Producto
        template_name = 'pagPrincipal.html'
        context_object_name = 'lista_productos'

        #Añadimos a la vista un listado de todos los pedidos existentes mediante la función get_context_data
        def get_context_data(self, **kwargs):
                context = super(ListadosListView, self).get_context_data(**kwargs)
                context['lista_pedidos'] = Pedido.objects.all()
                context['lista_clientes'] = Cliente.objects.all()
                context['lista_componentes'] = Componente.objects.all()
                return context

#Vista basada en clases que nos coge todos los atributos de un producto concreto para poder trabajar con ellos en el html
class ProductoDetailView(DetailView):
        model = Producto
        template_name = 'detalleProducto.html'
        context_object_name = 'detalle_producto'

#Vista basada en clases que nos coge todos los atributos de un pedido concreto para poder trabajar con ellos en el html
class PedidoDetailView(DetailView):
        model = Pedido
        template_name = 'detallePedido.html'
        context_object_name = 'detalle_pedido'

#Vista basada en clases que nos coge todos los atributos de un cliente concreto para poder trabajar con ellos en el html
class ClienteDetailView(DetailView):
        model = Cliente
        template_name = 'detalleCliente.html'
        context_object_name = 'detalle_cliente'

#Vista basada en clases que nos coge todos los atributos de un componente concreto para poder trabajar con ellos en el html
class ComponenteDetailView(DetailView):
        model = Componente
        template_name = 'detalleComponente.html'
        context_object_name = 'detalle_componente'

#Vista basada en clases que muestra un formulario para crear un producto, volver a mostrar el formulario con errores de validación (si los hay) y guardar el producto. La relación Pedido - Producto se deberá hacer en otro formulario debido al atributo 'cantidad'. La relación Producto - Componente se guarda al realizar este formulario.
class AnyadirProductoForm(CreateView):
        form_class = ProductoAnyadirForm
        template_name = 'anyadirProducto.html'
        success_url = reverse_lazy('pagPrincipal')

        def form_valid(self, form):
                self.object = form.save(commit=False)
                self.object.save()

                for componentes in form.cleaned_data['componentes']:
                        consta = Consta()
                        consta.producto = self.object
                        consta.componente = componentes
                        consta.save()

                return super(AnyadirProductoForm, self).form_valid(form)

#Vista basada en clases que muestra un formulario para crear un pedido, volver a mostrar el formulario con errores de validación (si los hay) y guardar el pedido. La relación Pedido - Producto se deberá hacer en otro formulario debido al atributo 'cantidad'.
class AnyadirPedidoForm(CreateView):
        form_class = PedidoAnyadirForm
        template_name = 'anyadirPedido.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases que muestra un formulario para crear un cliente, volver a mostrar el formulario con errores de validación (si los hay) y guardar el cliente.
class AnyadirClienteForm(CreateView):
        form_class = ClienteAnyadirForm
        template_name = 'anyadirCliente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases que muestra un formulario para crear un componente, volver a mostrar el formulario con errores de validación (si los hay) y guardar el componente.
class AnyadirComponenteForm(CreateView):
        form_class = ComponenteAnyadirForm
        template_name = 'anyadirComponente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases que muestra un formulario para asignar un pedido a un producto con su cantidad mediante la función 'get', volver a mostrar el formulario con errores de validación (si los hay) y guardar la relación a través de la función 'post'.
class AnyadirPedidoProductoForm(View):
        def get(self, request, *args, **kwargs):
                form = PedidoProductoAnyadirForm()
                context = {'form': form}
                return render(request, 'anyadirPedidoProducto.html', context)

        def post(self, request, *args, **kwargs):
                form = PedidoProductoAnyadirForm(request.POST)
                if form.is_valid():
                        compone = Compone()
                        compone.pedido = form.cleaned_data['pedido']
                        compone.producto = form.cleaned_data['producto']
                        compone.cantidad = form.cleaned_data['cantidad']
                        compone.save()
                        # Volvemos a la lista de departamentos
                        return redirect('pagPrincipal')
                return render(request, 'anyadirPedidoProducto.html', {'form': form})

#Vista basada en clases que muestra un formulario para asignar un componente a un producto mediante la función 'get', volver a mostrar el formulario con errores de validación (si los hay) y guardar la relación a través de la función 'post'.
class AnyadirComponenteProductoForm(View):
        def get(self, request, *args, **kwargs):
                form = ComponenteProductoAnyadirForm()
                context = {'form': form}
                return render(request, 'anyadirComponenteProducto.html', context)

        def post(self, request, *args, **kwargs):
                form = ComponenteProductoAnyadirForm(request.POST)
                if form.is_valid():
                        consta = Consta()
                        consta.producto = form.cleaned_data['producto']
                        consta.componente = form.cleaned_data['componente']
                        consta.save()
                        # Volvemos a la lista de departamentos
                        return redirect('pagPrincipal')
                return render(request, 'anyadirComponenteProducto.html', {'form': form})

#Vista basada en clases de tipo deleteView que nos vale para eliminar un producto
class EliminarProducto(DeleteView):
        model = Producto
        template_name = 'eliminarProducto.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases de tipo deleteView que nos vale para eliminar un pedido
class EliminarPedido(DeleteView):
        model = Pedido
        template_name = 'eliminarPedido.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases de tipo deleteView que nos vale para eliminar un cliente
class EliminarCliente(DeleteView):
        model = Cliente
        template_name = 'eliminarCliente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases de tipo deleteView que nos vale para eliminar un componente
class EliminarComponente(DeleteView):
        model = Componente
        template_name = 'eliminarComponente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos 
class ModificarPedido(UpdateView):
        model = Pedido
        template_name = 'modificarPedido.html'
        success_url = reverse_lazy('pagPrincipal')

        fields = {
                "fecha",
                "precioTotal",
                "cliente"
        }

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos 
class ModificarProducto(UpdateView):
        model = Producto
        template_name = 'modificarProducto.html'
        success_url = reverse_lazy('pagPrincipal')

        fields = {
                "nombre",
                "precio",
                "descripcion",
                "categoria",
                "componentes"
        }

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos 
class ModificarCliente(UpdateView):
        model = Cliente
        template_name = 'modificarCliente.html'
        success_url = reverse_lazy('pagPrincipal')

        fields = {
                "cif",
                "nombre",
                "telefono",
                "nombreEmpresa",
                "email"
        }

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos 
class ModificarComponente(UpdateView):
        model = Componente
        template_name = 'modificarComponente.html'
        success_url = reverse_lazy('pagPrincipal')

        fields = {
                "nombre",
                "marca"
        }