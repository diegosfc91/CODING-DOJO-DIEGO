#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6
print(matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

print(cantantes)

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"]= 9.9355431
print(coordenadas)

#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:
def iterarDiccionario(lista):
    # Iteramos sobre cada diccionario en la lista
    for diccionario in lista:
        # Para cada diccionario, iteramos sobre las llaves y valores
        for clave, valor in diccionario.items():
            print(f'"{clave}": "{valor}"')
        print()  # Línea en blanco para separar cada diccionario

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)

#BONUS: Que aparezcan en este formato:
#nombre - Ricky Martin, pais - Puerto Rico
#nombre - Chayanne, pais - Puerto Rico
#nombre - José José, pais - México
#nombre - Juan Luis Guerra, pais - República Dominicana

def iterarDiccionario(lista):
    # Iteramos sobre cada diccionario en la lista
    for diccionario in lista:
        resultado = ""  # Inicializamos la cadena donde construiremos el resultado
        # Usamos un bucle for tradicional para recorrer cada clave y valor del diccionario
        for clave in diccionario:
            valor = diccionario[clave]  # Obtenemos el valor correspondiente a la clave
            # Construimos la cadena agregando cada par clave-valor
            resultado += clave + " - " + valor + ", "  # No es necesario str(valor) porque sabemos que es una cadena
        # Eliminamos la última coma y espacio adicional al final de la cadena
        resultado = resultado[:-2]  # Cortamos los últimos dos caracteres (coma y espacio)
        print(resultado)  # Imprimimos el resultado en una sola línea

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:

#Ricky Martin
#Chayanne
#José José
#Juan Luis Guerra

def iterarDiccionario2(llave, lista):
    # Iteramos sobre cada diccionario en la lista
    for diccionario in lista:
        # Verificamos si la llave está en el diccionario
        if llave in diccionario:
            print(diccionario[llave])  # Imprimimos el valor de la llave especificada

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamada a la función
iterarDiccionario2("nombre", cantantes)


#Otro ejemplo: iterarDiccionario2(“pais”, cantantes) debe de imprimir:

#Puerto Rico
#Puerto Rico
#México
#República Dominicana

def iterarDiccionario2(llave, lista):
    # Iteramos sobre cada diccionario en la lista
    for diccionario in lista:
        # Verificamos si la llave está en el diccionario
        if llave in diccionario:
            print(diccionario[llave])  # Imprimimos el valor de la llave especificada

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamada a la función
iterarDiccionario2("pais", cantantes)


#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. Por ejemplo:
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        # Imprimimos el tamaño de la lista seguido del nombre de la clave en mayúsculas
        print(f"{len(lista)} {clave.upper()}")  # len(lista) da el tamaño de la lista
        # Imprimimos cada elemento de la lista en una nueva línea
        for valor in lista:
            print(valor)
        print()  # Imprimimos una línea en blanco para separar cada sección

imprimirInformacion(costa_rica)