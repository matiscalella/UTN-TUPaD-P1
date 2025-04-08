"""# TP 4 - Estructuras repetitivas
# Matias Scalella
# Ejercicio 1
for x in range(0, 101):
    print(x)

# Ejercicio 2
numero = int(input("Ingrese un numero entero para conocer la cantidad de digitos que lo componen: "))
cantidad_de_digitos = 0 # variable contadora de digitos
numero_ingresado = numero # Almaceno el valor ingresado para la impresion final del resultado, ya que la variable numero se transforma
if numero < 0: # Transformo el numero negativo, en positivo
    numero = (numero * -1)
if numero == 0: # Si el usuario ingresa 0, la respuesta debe ser 1 digito
    cantidad_de_digitos = 1

while numero != 0: # Estructura para contar la cantidad de digitos del numero utilizando un bucle de repeticion
    numero = numero // 10 
    cantidad_de_digitos += 1
print(f"El numero {numero_ingresado} tiene {cantidad_de_digitos} digitos.")

# Ejercicio 3
print("Hola, voy a sumar todos los numeros enteros comprendidos entre 2 numeros ingresados por vos.")
primer_numero = int(input("Ingresa el primer numero: "))
segundo_numero = int(input("Ingresa el segundo numero: "))
suma = 0
mayor = max(primer_numero, segundo_numero)
menor = min(primer_numero, segundo_numero)

for x in range(menor + 1, mayor): # la variable empieza con el menor valor, se suma a la variable de acumulacion, incrementa en 1 su valor y se suma hasta el valor mayor excluyente
    suma += x

print(f"La suma de los numeros enteros comprendidos entre {menor} y {mayor} es: {suma}")

# Ejercicio 4
print("Voy a sumar en orden todos los numeros que ingreses, hasta que ingreses un 0 (cero)")
numero = int(input("Ingresa un numero: "))
suma = numero

while numero != 0: # Mientras el numero ingresado sea distinto a cero, el bucle continua
    numero = int(input("Ingresa un numero para seguir sumando o un 0 (cero) para terminar: "))
    suma += numero # Suma el numero ingresado a la variable suma, que funciona como una variable de acumulacion

print(f"La suma de todos los numeros ingresados es: {suma}") # Cuando el numero ingresado es 0, se imprime el resultado de la variable de acumulacion

# Ejercicio 5
import random

print("Hola, en este juego tenes que adivinar un numero entre 0 y 9.")
numero_ganador = random.randint(0, 9) # almaceno un numero al azar del modulo random
numero_usuario = int(input("Ingresa un numero a ver si adivinas: ")) #primer intento del jugador
intentos = 1 # contador de intentos

while numero_usuario != numero_ganador:
    numero_usuario = int(input("Lo siento, ese no es el numero. Intenta nuevamente: ")) #si el usuario no acerto, se le pide un nuevo numero
    intentos += 1 # incrementador de intentos

print(f"Muy bien! \U0001F389 Acertaste!\nEs el numero: {numero_ganador} !\nAdivinaste en {intentos} intentos." ) # Mensaje que muestra el numero, los intentos y un emoji

# Ejercicio 6
for pares_de_cero_a_cien in range (100, -1, -2): # Con un bucle for inicio en 100, hasta el -1 (sin incluir) y con paso -2 (resta de a dos)
    print(pares_de_cero_a_cien)
"""
# Ejercicio 7

# Ejercicio 8
# Ejercicio 9
# Ejercicio 10

