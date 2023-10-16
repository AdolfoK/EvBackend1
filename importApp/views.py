from django.shortcuts import render, redirect
from importApp.models import Pedido

# Create your views here.

def simulacion_importacion(request):                 #Función que a través del metodo request adquiere datos.
    if request.method == 'POST':
        nombre_articulo = request.POST.get('nombre_articulo')
        codigo_articulo = request.POST.get('codigo_articulo')
        proveedor = request.POST.get('proveedor')
        cantidad_unidades = int(request.POST.get('cantidad_unidades'))
        costo_unitario_usd = float(request.POST.get('costo_unitario_usd'))
        costo_envio_usd = float(request.POST.get('costo_envio_usd'))
        
        #Calculos de impuestos y costos.
        total_pedido_usd = cantidad_unidades * costo_unitario_usd
        total_pedido_clp = total_pedido_usd * 890  # Suponiendo que 1 USD = 890 CLP
        costo_envio_clp = costo_envio_usd * 890  # Suponiendo que 1 USD = 890 CLP
        tasa_importacion_clp = total_pedido_clp * 0.06
        iva_clp = total_pedido_clp * 0.19
        impuesto_aduana_clp = tasa_importacion_clp + iva_clp
        costo_total_clp = total_pedido_clp + costo_envio_clp + impuesto_aduana_clp
        costo_total_usd = costo_total_clp / 890  # Suponiendo que 1 USD = 890 CLP
        
        #Instancia de Pedido y se guardarla en la base de datos.
        pedido = Pedido(
            nombre_articulo=nombre_articulo,
            codigo_articulo=codigo_articulo,
            proveedor=proveedor,
            cantidad_unidades=cantidad_unidades,
            costo_unitario_usd=costo_unitario_usd,
            costo_envio_usd=costo_envio_usd
        )
        
        # Guarda la instancia en la base de datos
        pedido.save()
        
        # Redirige al usuario a una página que muestre los resultados
        return render(request, 'importApp/resultados.html', {
            'nombre_articulo': nombre_articulo,
            'codigo_articulo': codigo_articulo,
            'proveedor': proveedor,
            'cantidad_unidades': cantidad_unidades,
            'costo_unitario_usd': costo_unitario_usd,
            'costo_envio_usd': costo_envio_usd,
            'total_pedido_usd': total_pedido_usd,
            'total_pedido_clp': total_pedido_clp,
            'costo_envio_clp': costo_envio_clp,
            'tasa_importacion_clp': tasa_importacion_clp,
            'iva_clp': iva_clp,
            'impuesto_aduana_clp': impuesto_aduana_clp,
            'costo_total_clp': costo_total_clp,
            'costo_total_usd': costo_total_usd,
        })

    # Si el método HTTP es GET, mostrar el formulario
    return render(request, 'importApp/formulario.html')

def resultados_simulacion(request):
    # Obtener el último pedido registrado
    ultimo_pedido = Pedido.objects.latest('id')

    return render(request, 'importApp/resultados.html', {'pedido': ultimo_pedido})