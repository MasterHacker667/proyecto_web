"""
URL configuration for pedidos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from obtener_pedidos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_carrito_ped/', views.agregar_carrito_ped),
    path('ver_pedidos/', views.ver_pedidos),
    path('eliminarPed/', views.eliminar_ped),
    path('ver_pedidos_cli/', views.verPed_cliente)
]
