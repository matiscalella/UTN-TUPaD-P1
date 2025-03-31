# TP3 Matias Scalella - Correr las tres comillas para verificar uno o uno los ejercicios
# Ejercicio 1 
"""
edad = int(input("Hola, ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
elif edad < 18 and edad >=0:
    print("No es mayor de edad")
else:
    print("Reinicie el programa.")

# Ejercicio 2
nota = float(input("Ingrese su nota: "))
mensaje = "Aprobado" if nota >= 6 else "Desaprobado"
print(mensaje)

# Ejercicio 3
numeroIngresado = float(input("Ingrese un numero par: "))
if numeroIngresado % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad <= 0:
    print("Ingrese su edad correctamente, reinicie el programa")
elif edad > 0 and edad < 12:
    print ("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# Ejercicio 5
contrasena = input("Hola, ingresa tu contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")"

# Ejercicio 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] # Este bloque de codigo crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
sesgo = ""

if moda < mediana < media  :
    sesgo = "Sesgo positivo o a la derecha"
elif moda > mediana > media:
    sesgo = "Sesgo negativo o a la izquierda"
elif moda == mediana == media:
    sesgo = "Sin sesgo"
else:
    sesgo = "En este caso no hay un sesgo claro"

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")
print(sesgo)

# Ejercicio 7
string = input("Hola, ingresa una palabra o frase: ")
if string[-1].lower() in ["a", "e", "i", "o", "u"]: #la funcion tomar el ultimo caracter y lo transforma en minuscula para compararlo con la lista de vocales
    print(string + "!")
else:
    print(string)
"""
# Ejercicio 8

# Ejercicio 9

# Ejercicio 10