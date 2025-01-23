from django.shortcuts import render
from .models import Venta
import matplotlib
matplotlib.use('Agg')  # Establece un backend sin interfaz gráfica
import matplotlib.pyplot as plt
import io
import urllib, base64
from datetime import datetime
from django.http import JsonResponse
from datetime import datetime
import random
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime
from django.shortcuts import render
from .models import Venta

def reporte_ventas_mensuales(request):
    # Consultar datos de ventas
    ventas = Venta.objects.all()

    # Filtrar por el mes actual
    mes_actual = datetime.now().month
    ventas_mes = ventas.filter(fecha__month=mes_actual)

    # Agrupar por vendedor y sumar las ventas
    ventas_por_vendedor = {}
    for venta in ventas_mes:
        ventas_por_vendedor[venta.vendedor] = ventas_por_vendedor.get(venta.vendedor, 0) + float(venta.monto)

    # Preparar datos para el gráfico
    vendedores = list(ventas_por_vendedor.keys())
    montos = list(ventas_por_vendedor.values())

    # Generar colores aleatorios o definidos
    colores = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FFD133']  # Lista fija de colores
    while len(colores) < len(vendedores):
        colores.append(f"#{random.randint(0, 0xFFFFFF):06x}")  # Generar más colores si hay más vendedores

    # Generar gráfico
    plt.bar(vendedores, montos, color=colores[:len(vendedores)])
    plt.title(f"Ventas del Mes ({datetime.now().strftime('%B')})")
    plt.xlabel("Vendedores")
    plt.ylabel("Monto de Ventas")
    plt.tight_layout()

    # Convertir gráfico a imagen
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()  # Cerrar figura para liberar memoria
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'queries/reporte.html', {'graphic': graphic})

def reporte_ventas_mensuales_json(request):
    # Consultar datos de ventas
    ventas = Venta.objects.all()

    # Filtrar por el mes actual
    mes_actual = datetime.now().month
    ventas_mes = ventas.filter(fecha__month=mes_actual)

    # Agrupar por vendedor y sumar las ventas
    ventas_por_vendedor = {}
    for venta in ventas_mes:
        ventas_por_vendedor[venta.vendedor] = ventas_por_vendedor.get(venta.vendedor, 0) + float(venta.monto)

    # Formatear datos para JSON
    data = {
        "labels": list(ventas_por_vendedor.keys()),
        "datasets": [{
            "label": f"Ventas del Mes ({datetime.now().strftime('%B')})",
            "data": list(ventas_por_vendedor.values()),
            "backgroundColor": ['#4CAF50', '#2196F3', '#FFC107', '#E91E63', '#9C27B0'],
            "borderColor": ['#388E3C', '#1976D2', '#FFA000', '#C2185B', '#7B1FA2'],
            "borderWidth": 1
        }]
    }

    return JsonResponse(data)
