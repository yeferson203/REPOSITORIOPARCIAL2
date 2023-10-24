from django.contrib import admin
from .models import Categoria, Talla, Producto, PedidoDetalle, Usuario, Factura, Pedido

admin.site.register(Categoria)
admin.site.register(Talla)
admin.site.register(Producto)
admin.site.register(PedidoDetalle)
admin.site.register(Usuario)
admin.site.register(Factura)
admin.site.register(Pedido)

# Registra tus modelos aquí
# Register your models here.
