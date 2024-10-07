'''a = int(input("Inserte Numero"))
b = int(input("Inserte Numero"))

def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

print(multiplicacion(a, b))

resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25'''


def buenos_dias(nombre):
   print("Buenos días "+nombre)

buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python