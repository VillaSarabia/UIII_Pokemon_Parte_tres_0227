from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto, Pedido
from django.utils import timezone
# ==========================================
# VISTA DE INICIO
# ==========================================
def inicio_Pokemon(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS PARA CLIENTES
# ==========================================
def agregar_cliente(request):
    if request.method == 'POST':
        try:
            # Verificar si el email ya existe
            email = request.POST['email']
            if Cliente.objects.filter(email=email).exists():
                mensaje_error = f"El email '{email}' ya está registrado. Por favor usa un email diferente."
                return render(request, 'clientes/agregar_cliente.html', {
                    'error_message': mensaje_error,
                    'form_data': request.POST
                })
            
            # Crear el cliente
            Cliente.objects.create(
                nombre_cliente=request.POST['nombre_cliente'],
                email=email,
                direccion=request.POST['direccion'],
                telefono=request.POST['telefono'],
                puntos_lealtad=int(request.POST['puntos_lealtad']),
                tipo_entrenador=request.POST['tipo_entrenador']
            )
            return redirect('ver_cliente')
            
        except Exception as e:
            # Manejar otros errores
            mensaje_error = f"Error al crear el cliente: {str(e)}"
            return render(request, 'clientes/agregar_cliente.html', {
                'error_message': mensaje_error,
                'form_data': request.POST
            })
    
    return render(request, 'clientes/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, cliente_id):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.nombre_cliente = request.POST['nombre_cliente']
        cliente.email = request.POST['email']
        cliente.direccion = request.POST['direccion']
        cliente.telefono = request.POST['telefono']
        cliente.puntos_lealtad = int(request.POST['puntos_lealtad'])
        cliente.tipo_entrenador = request.POST['tipo_entrenador']
        cliente.save()
        return redirect('ver_cliente')
    return redirect('ver_cliente')

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})

# ==========================================
# VISTAS PARA PRODUCTOS
# ==========================================
def agregar_producto(request):
    if request.method == 'POST':
        try:
            Producto.objects.create(
                nombre_producto=request.POST['nombre_producto'],
                descripcion=request.POST['descripcion'],
                precio=float(request.POST['precio']),
                cantidad_comprada=int(request.POST['cantidad_comprada']),
                categoria=request.POST['categoria'],
                generacion=int(request.POST['generacion']),
                es_legendario='es_legendario' in request.POST
            )
            return redirect('ver_producto')
        except Exception as e:
            mensaje_error = f"Error al crear el producto: {str(e)}"
            return render(request, 'productos/agregar_producto.html', {
                'error_message': mensaje_error,
                'form_data': request.POST
            })
    return render(request, 'productos/agregar_producto.html')

def ver_producto(request):
    productos = Producto.objects.all()
    return render(request, 'productos/ver_producto.html', {'productos': productos})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/actualizar_producto.html', {'producto': producto})

def realizar_actualizacion_producto(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.precio = float(request.POST['precio'])
        producto.cantidad_comprada = int(request.POST['cantidad_comprada'])
        producto.categoria = request.POST['categoria']
        producto.generacion = int(request.POST['generacion'])
        producto.es_legendario = 'es_legendario' in request.POST
        producto.save()
        return redirect('ver_producto')
    return redirect('ver_producto')

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'productos/borrar_producto.html', {'producto': producto})


# ==========================================
# VISTAS PARA PEDIDOS - 👈 ESTAS DEBEN EXISTIR
# ==========================================

def agregar_pedido(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        try:
            # Obtener cliente seleccionado
            cliente_id = request.POST['cliente']
            cliente = Cliente.objects.get(id=cliente_id)
            
            # Crear el pedido
            pedido = Pedido.objects.create(
                cliente=cliente,
                estado_pedido=request.POST['estado_pedido'],
                total_monto=float(request.POST['total_monto']),
                metodo_pago=request.POST['metodo_pago'],
                codigo_rastreo=request.POST['codigo_rastreo'],
                fecha_entrega_estimada=request.POST['fecha_entrega_estimada'] or None,
                es_pago_verificado='es_pago_verificado' in request.POST
            )
            
            # Asignar productos al pedido (si se seleccionaron)
            producto_ids = request.POST.getlist('productos')
            if producto_ids:
                productos_seleccionados = Producto.objects.filter(id__in=producto_ids)
                for producto in productos_seleccionados:
                    producto.pedido = pedido
                    producto.save()
            
            return redirect('ver_pedido')
            
        except Exception as e:
            mensaje_error = f"Error al crear el pedido: {str(e)}"
            return render(request, 'pedidos/agregar_pedido.html', {
                'error_message': mensaje_error,
                'clientes': clientes,
                'productos': productos,
                'form_data': request.POST
            })
    
    return render(request, 'pedidos/agregar_pedido.html', {
        'clientes': clientes,
        'productos': productos
    })

def ver_pedido(request):
    pedidos = Pedido.objects.all().select_related('cliente')
    return render(request, 'pedidos/ver_pedido.html', {'pedidos': pedidos})

def actualizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    return render(request, 'pedidos/actualizar_pedido.html', {
        'pedido': pedido,
        'clientes': clientes,
        'productos': productos
    })

def realizar_actualizacion_pedido(request, pedido_id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=pedido_id)
        cliente = Cliente.objects.get(id=request.POST['cliente'])
        
        pedido.cliente = cliente
        pedido.estado_pedido = request.POST['estado_pedido']
        pedido.total_monto = float(request.POST['total_monto'])
        pedido.metodo_pago = request.POST['metodo_pago']
        pedido.codigo_rastreo = request.POST['codigo_rastreo']
        pedido.fecha_entrega_estimada = request.POST['fecha_entrega_estimada'] or None
        pedido.es_pago_verificado = 'es_pago_verificado' in request.POST
        pedido.save()
        
        return redirect('ver_pedido')
    return redirect('ver_pedido')

def borrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedido')
    return render(request, 'pedidos/borrar_pedido.html', {'pedido': pedido})