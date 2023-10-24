from django.urls import path, include

from rest_framework import routers
from api import views 

# Definir el router
router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet,)
router.register(r'tallas', views.TallaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'pedidosdetalles', views.PedidoDetalleViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'facturas', views.FacturaViewSet)
router.register(r'pedidos', views.PedidoViewSet)



urlpatterns = [
    path('', include(router.urls)),


    
]
