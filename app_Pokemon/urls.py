from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Pokemon, name='inicio_Pokemon'),
    
    # URLs para Clientes
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver-cliente/', views.ver_cliente, name='ver_cliente'),
    path('actualizar-cliente/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('realizar-actualizacion-cliente/<int:cliente_id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('borrar-cliente/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Productos
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('ver-producto/', views.ver_producto, name='ver_producto'),
    path('actualizar-producto/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('realizar-actualizacion-producto/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('borrar-producto/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    
    # URLs para Pedidos
    path('agregar-pedido/', views.agregar_pedido, name='agregar_pedido'),
    path('ver-pedido/', views.ver_pedido, name='ver_pedido'),
    path('actualizar-pedido/<int:pedido_id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('realizar-actualizacion-pedido/<int:pedido_id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('borrar-pedido/<int:pedido_id>/', views.borrar_pedido, name='borrar_pedido'),
]