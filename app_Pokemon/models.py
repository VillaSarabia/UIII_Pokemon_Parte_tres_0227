from django.db import models

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    puntos_lealtad = models.IntegerField(default=0)
    tipo_entrenador = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_cliente

class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(
        max_length=50,
        choices=[('P', 'Pendiente'), ('E', 'Enviado'), ('T', 'Entregado')],
        default='P'
    )
    total_monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=50)
    codigo_rastreo = models.CharField(max_length=100, blank=True)
    fecha_entrega_estimada = models.DateField(null=True, blank=True)
    es_pago_verificado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Pedido N°{self.id} de {self.cliente.nombre_cliente}"

class Producto(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.SET_NULL,
        related_name='productos_en_pedido',
        null=True,
        blank=True
    )
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_comprada = models.IntegerField(default=1)
    categoria = models.CharField(max_length=50)
    generacion = models.IntegerField(default=1)
    es_legendario = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre_producto