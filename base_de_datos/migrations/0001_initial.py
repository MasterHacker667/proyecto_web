# Generated by Django 4.1.10 on 2023-10-15 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_Articulos', models.IntegerField()),
                ('precio_total', models.FloatField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_P', models.CharField(max_length=30)),
                ('apellido_M', models.CharField(max_length=30)),
                ('numero_clave', models.IntegerField()),
                ('Clabe', models.CharField(max_length=34)),
                ('cuenta_bancaria', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.BinaryField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('categoria', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=15)),
                ('precio', models.FloatField()),
                ('tamano', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Salones_Instituciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=50)),
                ('salon', models.CharField(max_length=30)),
                ('edificio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_P', models.CharField(max_length=30)),
                ('apellido_M', models.CharField(max_length=30)),
                ('numero_clave', models.IntegerField()),
                ('Clabe', models.CharField(max_length=34)),
                ('cuenta_bancaria', models.CharField(max_length=16)),
                ('paypal', models.CharField(max_length=2083)),
                ('disponibilidad', models.BooleanField()),
                ('estrellas_prom', models.FloatField()),
                ('foto_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.imagenes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='vendedor_salones_instituciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_salones_instituciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.salones_instituciones')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Salones_Instituciones_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
                ('id_salones_instituciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.salones_instituciones')),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.carrito')),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.productos')),
                ('id_Vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_Pedido', models.CharField(max_length=25)),
                ('entregado', models.BooleanField()),
                ('id_Carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.carrito')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes_Enviados_Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenido', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.chat')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes_Enviados_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenido', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.chat')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Imagenes_Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.imagenes')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Estrellas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrellas', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='ComprasRealizadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('cantidad', models.IntegerField()),
                ('precio_total', models.FloatField()),
                ('cambio', models.FloatField()),
                ('fecha', models.DateField()),
                ('codigo_secreto', models.IntegerField()),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.carrito')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Compras_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
                ('id_compras_realizadas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.comprasrealizadas')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes_Carritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.carrito')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='foto_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.imagenes'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.cliente'),
        ),
        migrations.AddField(
            model_name='chat',
            name='id_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_de_datos.vendedor'),
        ),
    ]
