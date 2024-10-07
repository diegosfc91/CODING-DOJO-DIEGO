#LISTAS
print("Hola a todos")
lista_vacia = []
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) # Imprime: Silvestre
gatos[1] = "Tom" # Reemplaza "Silvestre" por "Tom"
gatos.append("Felix")# Agrega al final "Felix"
print(gatos) # Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']
gatos.pop() # Elimina al ultimo elemento de la Lista
print(gatos) # Imprime: ['Garfield', 'Tom', 'Hello Kitty']
gatos.pop(1)# Elimina a "Tom"
print(gatos) # Imprime: ['Garfield', 'Hello Kitty']
print(gatos) # Imprime gatos por segunda vez

#TUPLAS
perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) #Imprime: Scooby Doo
#perro[2] = "comida de perro" #ERROR: Las tuplas no pueden ser modificadas (TypeError: 'tuple' object does not support item assignment)

#DICCIONARIOS
diccionario_vacio = {}
persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}
persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente
persona['hobbies'] = ['jugar videojuegos', 'programación'] # Agrega esa clave-valor si no existía previamente

print(persona) # Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor
print(altura) # Imprime: 1.71
print(persona) # salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 