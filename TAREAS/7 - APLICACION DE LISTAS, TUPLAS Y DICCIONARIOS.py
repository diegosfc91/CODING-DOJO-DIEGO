import math
# Lista de temperaturas diarias
temperaturas = [22.5, 21.0, 23.3, 25.2, 24.5]
media_temperatura = sum(temperaturas) / len(temperaturas)
print("Temperatura media:", media_temperatura)

# Coordenadas geográficas de una ubicación
coordenadas = (19.4326, -99.1332)  # Latitud y longitud de Ciudad de México

def calcular_distancia(coord1, coord2):
    # Implementación ficticia para calcular la distancia
    distancia = math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
    return distancia

distancia = calcular_distancia(coordenadas, (34.0522, -118.2437))
print(f"Distancia: {distancia:.1f}")

# Diccionario con información sobre un conjunto de datos
dataset_info = {
    "nombre": "Datos de ventas",
    "columnas": ["fecha", "producto", "cantidad", "precio"],
    "filas": 1000,
    "fuente": "Sistema de ventas interno"
}

print("Nombre del conjunto de datos:", dataset_info["nombre"])
print("Número de filas:", dataset_info["filas"])