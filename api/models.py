from django.db import models

class Categoria(models.Model):
    descripcion = models.CharField(max_length=255)

class Talla(models.Model):
    descripcion = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    disponibilidad_stock = models.IntegerField()

class PedidoDetalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class Usuario(models.Model):
    contrasena = models.CharField(max_length=255)
    roll_id = models.IntegerField()
    identificacion_usuario = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

class Factura(models.Model):
    numero_factura = models.CharField(max_length=50, unique=True)
    fecha_factura = models.DateField()
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    fecha_pedido = models.DateField()
    estado_del_pedido = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido_detalle = models.ForeignKey(PedidoDetalle, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)



# Create your models here.
