from django.contrib import admin
from .models import Cliente, Pedido, Producto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre_cliente', 'email', 'telefono', 'puntos_lealtad', 'tipo_entrenador']
    search_fields = ['nombre_cliente', 'email']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha_pedido', 'estado_pedido', 'total_monto', 'es_pago_verificado']
    list_filter = ['estado_pedido', 'fecha_pedido', 'es_pago_verificado']
    search_fields = ['cliente__nombre_cliente', 'codigo_rastreo']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'precio', 'categoria', 'generacion', 'es_legendario', 'cantidad_comprada']
    list_filter = ['categoria', 'generacion', 'es_legendario']
    search_fields = ['nombre_producto', 'categoria']