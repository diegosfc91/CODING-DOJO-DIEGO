def multiplica_por_2(n):
    lista = []
    for i in range(n+1):
        lista.append(i*2)
    return lista


# Ejemplo de uso
n = int(input("Introduzca numero"))
print(multiplica_por_2(n))  # Salida: [0, 2, 4, 6, 8, 10]


#Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
#Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]

def valor_multiplicado_longitud(valor, longitud):
    valormultiplicado = valor * longitud
    lista = []
    for i in range (longitud):
        lista.append(valormultiplicado)
    return lista

valor = int(input("Introduzca valor"))
longitud = int(input("Introduzca longitud"))
print(valor_multiplicado_longitud(valor, longitud))