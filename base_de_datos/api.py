from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
class ImagenesViewSets(viewsets.ModelViewSet):
    queryset = Imagenes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImagenesSerializer
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VendedorSerializer
class SeguidoresViewSet(viewsets.ModelViewSet):
    queryset = Seguidores.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SeguidoresSerializer
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarritoSerializer
class ComprasRealizadasViewSet(viewsets.ModelViewSet):
    queryset = ComprasRealizadas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComprasRealizadasSerializer
class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosSerializer
class Producto_VendedorViewSet(viewsets.ModelViewSet):
    queryset = Producto_Vendedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Producto_VendedorSerializer
class Producto_CarritoViewSet(viewsets.ModelViewSet):
    queryset = Productos_Carrito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Producto_CarritoSerializer
class Salones_InstitucionesViewSet(viewsets.ModelViewSet):
    queryset = Salones_Instituciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Salones_InstitucionesSerializer
class Salones_Instituciones_ClienteViewSet(viewsets.ModelViewSet):
    queryset = Salones_Instituciones_Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class= Salones_Instituciones_ClienteSerializer
class vendedor_salones_institucionesViewSet(viewsets.ModelViewSet):
    queryset = vendedor_salones_instituciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = vendedor_salones_institucionesSerializer
class Compras_ClienteViewSet(viewsets.ModelViewSet):
    queryset = Compras_Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Compras_ClienteSerializer

class Clientes_CarritosViewSet(viewsets.ModelViewSet):
    queryset = Clientes_Carritos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Clientes_CarritosSerializer

class EstrellasViewSet(viewsets.ModelViewSet):
    queryset = Estrellas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstrellasSerializer

class Imagenes_ProductosViewSet(viewsets.ModelViewSet):
    queryset = Imagenes_Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Imagenes_ProductosSerializer

class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidosSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ChatSerializer

class Mensajes_Enviados_VendedorViewSet(viewsets.ModelViewSet):
    queryset = Mensajes_Enviados_Vendedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Mensajes_Enviados_VendedorSerializer

class Mensajes_Enviados_ClienteViewSet(viewsets.ModelViewSet):
    queryset = Mensajes_Enviados_Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Mensajes_Enviados_ClienteSerializer