from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView,TemplateView
from django.views import View
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .forms import *
from .models import *

class RegistroView(CreateView):
        form_class = RegistroForm
        template_name = 'registration/register.html'
        success_url = reverse_lazy('pagPrincipal')

        #Con esta función la relación Producto - Componente se guarda al realizar este formulario.
        def form_valid(self, form):
                self.object = form.save(commit=False)
                self.object.save()

                self.object.groups.add(form.cleaned_data['group'])

                return super(RegistroView, self).form_valid(form)



#Vista basada en clases que nos coge un listado de todos los productos para poder trabajar con ellos en el html
class ListadosListView(ListView):
        model = Producto
        template_name = 'pagPrincipal.html'
        context_object_name = 'lista_productos'

        #Añdimos a la vista un listado de todos los pedidos, clientes y componentes existentes mediante la función get_context_data
        def get_context_data(self, **kwargs):
                context = super(ListadosListView, self).get_context_data(**kwargs)
                context['lista_pedidos'] = Pedido.objects.all()
                context['lista_clientes'] = Cliente.objects.all()
                context['lista_componentes'] = Componente.objects.all()
                
                #acontinuacion esta todo la paginacion de la 4 listas, se recupera el numero de paginas y la pagina actual por cada uno, se muestran solo 3 registros por pagina
                paginator = Paginator(Producto.objects.all(), 3)
                # Si no existe la variable page en la url entonces sera 1
                context['paginaProducto'] = self.request.GET.get('paginaProducto') or 1
                paginaProducto = context['paginaProducto']    
                productos = paginator.get_page(paginaProducto)
                context['productos'] = productos
                context['pagina_actualProducto'] = int(paginaProducto)
                context['paginasProducto'] = range(1, productos.paginator.num_pages + 1)

                paginator = Paginator(Pedido.objects.all(), 3)
                # Si no existe la variable page en la url entonces sera 1
                context['paginaPedido'] = self.request.GET.get('paginaPedido') or 1
                paginaPedido = context['paginaPedido']
                pedidos = paginator.get_page(paginaPedido)
                context['pedidos'] = pedidos
                context['pagina_actualPedido'] = int(paginaPedido)
                context['paginasPedido'] = range(1, pedidos.paginator.num_pages + 1)

                paginator = Paginator(Cliente.objects.all(), 3)
                # Si no existe la variable page en la url entonces sera 1
                context['paginaCliente'] = self.request.GET.get('paginaCliente') or 1
                paginaCliente = context['paginaCliente']
                clientes = paginator.get_page(paginaCliente)
                context['clientes'] = clientes
                context['pagina_actualCliente'] = int(paginaCliente)
                context['paginasCliente'] = range(1, clientes.paginator.num_pages + 1)

                paginator = Paginator(Componente.objects.all(), 3)
                # Si no existe la variable page en la url entonces sera 1
                context['paginaComponente'] = self.request.GET.get('paginaComponente') or 1
                paginaComponente = context['paginaComponente']
                componentes = paginator.get_page(paginaComponente)
                context['componentes'] = componentes
                context['pagina_actualComponente'] = int(paginaComponente)
                context['paginasComponente'] = range(1, componentes.paginator.num_pages + 1)

                return context


#Vista basada en clases que nos coge todos los atributos de un producto concreto para poder trabajar con ellos en el html. El 'permission_required' es para que un usuario sin autorización no pueda acceder a esta información por URL.
class ProductoDetailView(PermissionRequiredMixin, DetailView):
        permission_required = 'appGestionDePedidos.view_producto'
        model = Producto
        template_name = 'detalleProducto.html'
        context_object_name = 'detalle_producto'

#Vista basada en clases que nos coge todos los atributos de un pedido concreto para poder trabajar con ellos en el html. El 'permission_required' es para que un usuario sin autorización no pueda acceder a esta información por URL.
class PedidoDetailView(PermissionRequiredMixin, DetailView):
        permission_required = 'appGestionDePedidos.view_pedido'
        model = Pedido
        template_name = 'detallePedido.html'
        context_object_name = 'detalle_pedido'

#Vista basada en clases que nos coge todos los atributos de un cliente concreto para poder trabajar con ellos en el html. El 'permission_required' es para que un usuario sin autorización no pueda acceder a esta información por URL.
class ClienteDetailView(PermissionRequiredMixin, DetailView):
        permission_required = 'appGestionDePedidos.view_cliente'
        model = Cliente
        template_name = 'detalleCliente.html'
        context_object_name = 'detalle_cliente'

#Vista basada en clases que nos coge todos los atributos de un componente concreto para poder trabajar con ellos en el html. El 'permission_required' es para que un usuario sin autorización no pueda acceder a esta información por URL.
class ComponenteDetailView(PermissionRequiredMixin, DetailView):
        permission_required = 'appGestionDePedidos.view_componente'
        model = Componente
        template_name = 'detalleComponente.html'
        context_object_name = 'detalle_componente'

#Vista basada en clases que muestra un formulario para crear un producto, volver a mostrar el formulario con errores de validación (si los hay) y guardar el producto. La relación Pedido - Producto se deberá hacer en otro formulario debido al atributo 'cantidad'. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class AnyadirProductoForm(PermissionRequiredMixin, CreateView):
        permission_required = 'appGestionDePedidos.add_producto'
        form_class = ProductoAnyadirForm
        template_name = 'anyadirProducto.html'
        success_url = reverse_lazy('pagPrincipal')

        #Con esta función la relación Producto - Componente se guarda al realizar este formulario.
        def form_valid(self, form):
                self.object = form.save(commit=False)
                self.object.save()

                for componentes in form.cleaned_data['componentes']:
                        consta = Consta()
                        consta.producto = self.object
                        consta.componente = componentes
                        consta.save()

                return super(AnyadirProductoForm, self).form_valid(form)

#Vista basada en clases que muestra un formulario para crear un pedido, volver a mostrar el formulario con errores de validación (si los hay) y guardar el pedido. La relación Pedido - Producto se deberá hacer en otro formulario debido al atributo 'cantidad'. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class AnyadirPedidoForm(PermissionRequiredMixin, CreateView):
        permission_required = 'appGestionDePedidos.add_pedido'
        form_class = PedidoAnyadirForm
        template_name = 'anyadirPedido.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases que muestra un formulario para crear un cliente, volver a mostrar el formulario con errores de validación (si los hay) y guardar el cliente. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class AnyadirClienteForm(PermissionRequiredMixin, CreateView):
        permission_required = 'appGestionDePedidos.add_cliente'
        form_class = ClienteAnyadirForm
        template_name = 'anyadirCliente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases que muestra un formulario para crear un componente, volver a mostrar el formulario con errores de validación (si los hay) y guardar el componente. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class AnyadirComponenteForm(PermissionRequiredMixin, CreateView):
        permission_required = 'appGestionDePedidos.add_componente'
        form_class = ComponenteAnyadirForm
        template_name = 'anyadirComponente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases que muestra un formulario para asignar un pedido a un producto con su cantidad mediante la función 'get', volver a mostrar el formulario con errores de validación (si los hay) y guardar la relación a través de la función 'post'. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class AnyadirPedidoProductoForm(PermissionRequiredMixin, View):
        permission_required = 'appGestionDePedidos.add_compone'
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

#Vista basada en clases que muestra un formulario para asignar un componente a un producto mediante la función 'get', volver a mostrar el formulario con errores de validación (si los hay) y guardar la relación a través de la función 'post'. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class AnyadirComponenteProductoForm(PermissionRequiredMixin, View):
        permission_required = 'appGestionDePedidos.add_consta'
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

#Vista basada en clases de tipo deleteView que nos vale para eliminar un producto. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class EliminarProducto(PermissionRequiredMixin, DeleteView):
        permission_required = 'appGestionDePedidos.delete_producto'
        model = Producto
        template_name = 'eliminarProducto.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases de tipo deleteView que nos vale para eliminar un pedido. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class EliminarPedido(PermissionRequiredMixin, DeleteView):
        permission_required = 'appGestionDePedidos.delete_pedido'
        model = Pedido
        template_name = 'eliminarPedido.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases de tipo deleteView que nos vale para eliminar un cliente. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class EliminarCliente(PermissionRequiredMixin, DeleteView):
        permission_required = 'appGestionDePedidos.delete_cliente'
        model = Cliente
        template_name = 'eliminarCliente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clases de tipo deleteView que nos vale para eliminar un componente. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class EliminarComponente(PermissionRequiredMixin, DeleteView):
        permission_required = 'appGestionDePedidos.delete_componente'
        model = Componente
        template_name = 'eliminarComponente.html'
        success_url = reverse_lazy('pagPrincipal')

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class ModificarPedido(PermissionRequiredMixin, UpdateView):
        permission_required = 'appGestionDePedidos.change_pedido'
        model = Pedido
        template_name = 'modificarPedido.html'
        success_url = reverse_lazy('pagPrincipal')

        fields = {
                "fecha",
                "precioTotal",
                "cliente"
        }

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class ModificarProducto(PermissionRequiredMixin, UpdateView):
        permission_required = 'appGestionDePedidos.change_producto'
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

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class ModificarCliente(PermissionRequiredMixin, UpdateView):
        permission_required = 'appGestionDePedidos.change_cliente'
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

#Vista basada en clase tipo UpdateView, si le indicamos que campos queremos modificar (en fields) los muestra por pantalla y no modifica los que no le indicamos. El 'permission_required' es para que un usuario sin autorización no pueda acceder a este formulario por URL.
class ModificarComponente(PermissionRequiredMixin, UpdateView):
        permission_required = 'appGestionDePedidos.change_componente'
        model = Componente
        template_name = 'modificarComponente.html'
        success_url = reverse_lazy('pagPrincipal')

        fields = {
                "nombre",
                "marca"
        }

#Vista que permite buscar si existe algun producto que coincida con la busqueda.
class BuscarProductoView(TemplateView):
        permission_required = 'appGestionDePedidos.search'

        def post(self, request, *args, **kwargs):
                buscarProducto = request.POST['lupa']
                productos = Producto.objects.filter(nombre__contains=buscarProducto)
                
                return render(request, 'buscar/resultadosBusqueda.html',{'productos':productos})

#Vista que permite buscar si existe algun cliente que coincida con la busqueda.
class BuscarClienteView(TemplateView):
        permission_required = 'appGestionDePedidos.search'

        def post(self, request, *args, **kwargs):
                buscarCliente = request.POST['lupa']
                clientes = Cliente.objects.filter(nombre__contains=buscarCliente)
                
                return render(request, 'buscar/resultadosBusqueda.html',{'clientes':clientes})

#Vista que permite buscar si existe algun componente que coincida con la busqueda.
class BuscarComponenteView(TemplateView):
        permission_required = 'appGestionDePedidos.search'

        def post(self, request, *args, **kwargs):
                buscarComponente = request.POST['lupa']
                componentes = Componente.objects.filter(nombre__contains=buscarComponente)
                
                return render(request, 'buscar/resultadosBusqueda.html',{'componentes':componentes})

#Vista que permite buscar si existe algun pedido que coincida con la busqueda.
class BuscarPedidoView(TemplateView):
        permission_required = 'appGestionDePedidos.search'

        def post(self, request, *args, **kwargs):
                buscarPedido = request.POST['lupa']
                pedidos = Pedido.objects.filter(fecha__contains=buscarPedido)
                
                return render(request, 'buscar/resultadosBusqueda.html',{'pedidos':pedidos})

#Vista que permite realizar el envío del mensaje al correo predeterminado
class EnviarCorreoView(TemplateView):
        template_name = 'contacto.html'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['EnviarMail_form'] = EnviarMail()

                return context
        
        def post(self, request, *args, **kwargs):
                Nombre = request.POST.get('Nombre')
                Apellidos = request.POST.get('Apellidos')
                Email = request.POST.get('Email')
                Mensaje = request.POSR.get('Mensaje')

                Correo = render_to_string(
                        'email_content.html', {
                        'Nombre': Nombre,
                        'Apellidos': Apellidos,
                        'Email': Email,
                        'Mensaje': Mensaje,
                        },
                )
                
                email_message = EmailMessage(
                        subject = 'Mensaje de un usuario',
                        body = Correo,
                        from_email = Email,
                        to=['duestronicomponents@gmail.com'],
                )
                email_message.content_subtype = 'html'
                email_message.send()

                return redirect('pagPrincipal')