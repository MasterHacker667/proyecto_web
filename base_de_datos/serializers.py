from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}
class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'
class SeguidoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguidores
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'
class ComprasRealizadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprasRealizadas
        fields = '__all__'
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
class Producto_VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_Vendedor
        fields = '__all__'
class Producto_CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos_Carrito
        fields = '__all__'
class Salones_InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salones_Instituciones
        fields = '__all__'
class Salones_Instituciones_ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salones_Instituciones_Cliente
        fields = '__all__'
class vendedor_salones_institucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendedor_salones_instituciones
        fields = '__all__'
class Compras_ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras_Cliente
        fields = '__all__'
class Clientes_CarritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes_Carritos
        fields = '__all__'
class EstrellasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrellas
        fields = '__all__'
class Imagenes_ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes_Productos
        fields = '__all__'
class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
class Mensajes_Enviados_VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes_Enviados_Vendedor
        fields = '__all__'
class Mensajes_Enviados_ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensajes_Enviados_Cliente
        fields = '__all__'
