from rest_framework import routers
from .api import *

router  = routers.DefaultRouter()
router.register('api/user', UserViewSets, 'users')
router.register('api/images', ImagenesViewSets, 'imagenes')
router.register('api/clientes', ClienteViewSet, 'cientes')
router.register('api/vendedor', VendedorViewSet, 'vendedores')
router.register('api/carrito', CarritoViewSet, 'carrito')
router.register('api/compras_realizadas', ComprasRealizadasViewSet, 'Compras_Realizadas')
router.register('api/productos', ProductosViewSet, 'productos')
router.register('api/producto_vendedor', Producto_VendedorViewSet, 'productoVendedor')
router.register('api/producto_carrito', Producto_CarritoViewSet, 'producto_Carrito')
router.register('api/salones_instituciones', Salones_InstitucionesViewSet, 'salonesInstituciones')
router.register('api/salones_instituciones_cliente', Salones_Instituciones_ClienteViewSet, 'Salones_Instituciones_Cliente')
router.register('api/vendedor_salones_instituciones', vendedor_salones_institucionesViewSet, 'vendedor_salones_instituciones')
router.register('api/compras_cliente', Compras_ClienteViewSet, "Compras_Cliente")
router.register('api/clientes_carritos', Clientes_CarritosViewSet, 'Clientes_Carritos')
router.register('api/estrellas', EstrellasViewSet, 'estrellas')
router.register('api/imagenes_productos', Imagenes_ProductosViewSet, 'Imagenes_Productos')
router.register('api/pedidos', PedidosViewSet, 'pedidos')
router.register('api/chat', ChatViewSet, 'chat')
router.register('api/mensajes_enviados_vendedor', Mensajes_Enviados_VendedorViewSet, 'Mensajes_Enviados_Vendedor')
router.register('api/mensajes_enviados_cliene', Mensajes_Enviados_ClienteViewSet, 'Mensajes_Enviados_ClienteViewSet')

urlpatterns = router.urls