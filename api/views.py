from rest_framework import viewsets
from .models import Categoria, Talla, Producto, PedidoDetalle, Usuario, Factura, Pedido
from .serializer import (
    CategoriaSerializer, TallaSerializer, ProductoSerializer,
    PedidoDetalleSerializer, UsuarioSerializer, FacturaSerializer, PedidoSerializer
)
from rest_framework.routers import DefaultRouter

# Definir ViewSets para tus modelos
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TallaViewSet(viewsets.ModelViewSet):
    queryset = Talla.objects.all()
    serializer_class = TallaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PedidoDetalleViewSet(viewsets.ModelViewSet):
    queryset = PedidoDetalle.objects.all()
    serializer_class = PedidoDetalleSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


# Create your views here.
