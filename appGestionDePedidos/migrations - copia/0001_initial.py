# Generated by Django 3.2 on 2021-04-21 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.CharField(max_length=5)),
                ('cif', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=9)),
                ('nombreEmpresa', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_componente', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.CharField(max_length=5)),
                ('precio', models.IntegerField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('componente', models.ManyToManyField(to='appGestionDePedidos.Componente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.CharField(max_length=5)),
                ('fecha', models.CharField(max_length=50)),
                ('precioTotal', models.IntegerField(max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGestionDePedidos.cliente')),
                ('producto', models.ManyToManyField(to='appGestionDePedidos.Producto')),
            ],
        ),
    ]
