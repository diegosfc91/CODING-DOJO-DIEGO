x = 10 #tipo numerico
y = 0.7#tipo flotante

print(type(x))
print(type(y))

entero_a_decimal = float(123)
decimal_a_entero = int(22.5)
entero_a_complejo = complex(35)

print(entero_a_decimal) #Imprime: 123.0
print(decimal_a_entero) #Imprime: 22
print(entero_a_complejo) #Imprime: (35+0j)

import random
num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
print(num_aleatorio) #Imprime el número aleatorio generado