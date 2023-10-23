from django.db import models
from django.contrib.auth.models import User

class Imagenes(models.Model):
    imagen = models.BinaryField(blank=True, null= True)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ForeignKey(Imagenes, on_delete=models.CASCADE)
    numero_clave = models.IntegerField() #Este es el numero secreto para encriptar cosas
    Clabe = models.CharField(max_length=34)
    cuenta_bancaria = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    #__str__(self): #Este metodo solo es en caso de que querramos acceder a toda la informacion desde el shell
        #return 'User: %s \nFoto Perfil %s \napellido_P: %s'%(self.user.username, self.foto_perfil, self.apellido_P)

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ForeignKey(Imagenes, on_delete=models.CASCADE)
    numero_clave = models.IntegerField() #Este es el numero secreto para encriptar cosas
    Clabe = models.CharField(max_length=34)
    cuenta_bancaria = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)
    client_id_paypal = models.CharField(max_length=2000)
    client_secret_paypal = models.CharField(max_length=2000)
    stripe_secret_key = models.CharField(max_length=1000)
    stripe_publishable_key = models.CharField(max_length=1000)
    disponibilidad = models.BooleanField()
    estrellas_prom = models.FloatField()

class Seguidores(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Carrito(models.Model):
    No_Articulos = models.IntegerField()
    precio_total = models.FloatField()
    nombre = models.CharField(max_length=50)

class ComprasRealizadas(models.Model):
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    cantidad = models.IntegerField()
    precio_total = models.FloatField()
    cambio = models.FloatField()
    fecha = models.DateField()
    codigo_secreto = models.IntegerField()

class Productos(models.Model):
    nombre = models.CharField(max_length=25)
    categoria = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=500)
    color = models.CharField(max_length=15)
    precio = models.FloatField()
    tamano = models.CharField(max_length=15)

class Producto_Vendedor(models.Model):
    id_Producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    id_Vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Productos_Carrito(models.Model):
    id_Carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_Producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

class Salones_Instituciones(models.Model):
    institucion = models.CharField(max_length=50)
    salon = models.CharField(max_length=30)
    edificio = models.CharField(max_length=50)

class Salones_Instituciones_Cliente(models.Model):
    id_salones_instituciones = models.ForeignKey(Salones_Instituciones, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class vendedor_salones_instituciones(models.Model):
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_salones_instituciones = models.ForeignKey(Salones_Instituciones, on_delete=models.CASCADE)

class Compras_Cliente(models.Model):
    id_compras_realizadas = models.ForeignKey(ComprasRealizadas, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Clientes_Carritos(models.Model):
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Estrellas(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    estrellas = models.IntegerField()

class Imagenes_Productos(models.Model):
    id_imagen = models.ForeignKey(Imagenes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

#Pedidos:
class Pedidos(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_Carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    No_Pedido = models.CharField(max_length=25)
    entregado = models.BooleanField()
#Chats:
class Chat(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

class Mensajes_Enviados_Cliente(models.Model):
    emisor = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    Contenido = models.CharField(max_length=300)
    fecha = models.DateField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class Mensajes_Enviados_Vendedor(models.Model):
    emisor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Contenido = models.CharField(max_length=300)
    fecha = models.DateField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)