
from django.contrib import admin
from django.urls import path, include
from base_de_datos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_de_datos.urls')),
    #Vistas
    path('vendedor/id_user/<int:id_user>/', views.obtener_vendedor, name="obtener_vendedor_id_user"),
    path('cliente/id_cliente/<int:id_cliente>', views.obtener_cliente_datos_bancarios, name="Obtener_datos_bancarios")
]
