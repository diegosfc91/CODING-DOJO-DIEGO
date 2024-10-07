ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 3, "precio": 1200.50},
    {"fecha": "2024-01-02", "producto": "Mouse", "cantidad": 10, "precio": 25.75},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 5, "precio": 45.60},
    {"fecha": "2024-01-04", "producto": "Monitor", "cantidad": 2, "precio": 300.99},
    {"fecha": "2024-01-05", "producto": "Impresora", "cantidad": 1, "precio": 150.00},
    {"fecha": "2024-01-06", "producto": "Smartphone", "cantidad": 4, "precio": 750.00}
]

# Imprimir la lista de ventas
for venta in ventas:
    print(venta)

ventas_totales = 0
for i in range(len(ventas)):
    ventas_totales = ventas[i]["cantidad"] * ventas[i]["precio"]+ventas_totales
print(ventas_totales)

# Crear el diccionario ventas_por_producto
ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

# Identificar el producto con la mayor cantidad vendida
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# Mostrar resultados
print("Ventas por producto:", ventas_por_producto)
print("Producto más vendido:", producto_mas_vendido, "con", ventas_por_producto[producto_mas_vendido], "unidades vendidas.")

# Crear el diccionario precios_por_producto
precios_por_producto = {}

# Recorrer la lista de ventas para agregar los datos al diccionario
for venta in ventas:
    producto = venta["producto"]
    total_precio = venta["precio"] * venta["cantidad"]
    cantidad = venta["cantidad"]
    
    if producto not in precios_por_producto:
        precios_por_producto[producto] = (total_precio, cantidad)
    else:
        # Actualizar la suma de precios y cantidad de unidades vendidas
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + total_precio,
            precios_por_producto[producto][1] + cantidad
        )

# Calcular el precio promedio de venta para cada producto
precio_promedio_por_producto = {producto: total_precio / cantidad for producto, (total_precio, cantidad) in precios_por_producto.items()}

print("Diccionario de precios por producto:", precios_por_producto)
print("Precio promedio por producto:", precio_promedio_por_producto)


# Crear el diccionario ingresos_por_dia
ingresos_por_dia = {}

# Calcular los ingresos totales por día y almacenarlos en el diccionario
for venta in ventas:
    fecha = venta["fecha"]
    total_precio = venta["precio"] * venta["cantidad"]
    
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = total_precio
    else:
        # Sumar el precio total de la venta a la fecha correspondiente
        ingresos_por_dia[fecha] += total_precio

print("Ingresos por día:", ingresos_por_dia)

# Crear el diccionario resumen_ventas
resumen_ventas = {}
# Calcular la cantidad total, ingresos totales y precio promedio para cada producto
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    total_precio = venta["precio"] * cantidad
    
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": cantidad,
            "ingresos_totales": total_precio,
            "precio_promedio": venta["precio"]
        }
    else:
        # Actualizar la cantidad total y los ingresos totales
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += total_precio
        # Calcular el nuevo precio promedio
        resumen_ventas[producto]["precio_promedio"] = resumen_ventas[producto]["ingresos_totales"] / resumen_ventas[producto]["cantidad_total"]

# Mostrar el resumen de ventas
print("Resumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"{producto}: {datos}")