
from django.contrib import admin
from django.urls import path, include
from base_de_datos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_de_datos.urls')),
    #Vistas
    path('vendedor/id_user/<int:id_user>/', views.obtener_vendedor, name="obtener_vendedor_id_user"),
    path('cliente/id_cliente/<int:id_cliente>', views.obtener_cliente_datos_bancarios, name="Obtener_datos_bancarios"),
    path('auth_user/', views.autenticar_usuario, name="auth_user"),
    path('delete_clientes_carritos/<int:record_id>', views.delete_cliente_carritos),
    path('delete/delete_productos_carrito/<int:record_id>', views.delete_productos_carrito),
    path('delete/delete_carrito/<int:record_id>', views.delete_carrito),
    path('update/carrito_precio/', views.modificar_carrito),
    path('delete/pedido/<int:record_id>', views.delete_pedido),
    path('verUsers_id/', views.Usuario1)
]
