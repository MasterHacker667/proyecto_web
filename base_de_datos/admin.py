from django.contrib import admin
from base_de_datos.models import *
from django.contrib.auth.models import User
# Register your models here.
#admin.site.register(User)
admin.site.register(Cliente)
admin.site.register(Imagenes)
admin.site.register(Vendedor)
admin.site.register(Carrito)
admin.site.register(ComprasRealizadas)
admin.site.register(Productos)
admin.site.register(Producto_Vendedor)
admin.site.register(Productos_Carrito)
admin.site.register(Salones_Instituciones)
admin.site.register(Salones_Instituciones_Cliente)
admin.site.register(vendedor_salones_instituciones)
admin.site.register(Compras_Cliente)
admin.site.register(Clientes_Carritos)
admin.site.register(Estrellas)
admin.site.register(Imagenes_Productos)
admin.site.register(Pedidos)
admin.site.register(Chat)
admin.site.register(Mensajes_Enviados_Cliente)
admin.site.register(Mensajes_Enviados_Vendedor)