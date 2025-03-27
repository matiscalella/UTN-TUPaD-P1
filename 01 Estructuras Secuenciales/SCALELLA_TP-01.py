# Trabajo practico 1 SECUENCIALES - Matias Scalella
# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese nu nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Hola, ingrese su nombre: ")
apellido = input("Tambien necesito saber su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("¿Cual es tu lugar de residencia? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
import math #Esta funcion la consegui googleando, al igual que round() para redondear el resultado a 2 decimales
print("Hola, soy un programa que calcula el area y el perimetro de cualquier circulo.")
radio = float(input("Ingresa el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = math.pi * radio * 2
print(f"El area del circulo es {round(area, 2)} y su perimetro es {round(perimetro, 2)}")"

# Ejercicio 5
print("Hola soy un programa que convierte segundos a horas.")
segundos = int(input("Ingrese la cantidad de segundos que deseas convertir: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {round(horas, 2)} horas.")"

# Ejercicio 6
numero = int(input("Hola, ingresa un numero: "))
print(f"La tabla de multiplicar del {numero} es:")
print(f"1 x {numero} = ", numero * 1 )
print(f"2 x {numero} = ", numero * 2 )
print(f"3 x {numero} = ", numero * 3 )
print(f"4 x {numero} = ", numero * 4 )
print(f"5 x {numero} = ", numero * 5 )
print(f"6 x {numero} = ", numero * 6 )
print(f"7 x {numero} = ", numero * 7 )
print(f"8 x {numero} = ", numero * 8 )
print(f"9 x {numero} = ", numero * 9 )"

# Ejercicio 7
print("Hola, ingrese dos números enteros distintos del 0: ")
num1 = int(input())
num2 = int(input())
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2
print(f"{num1} + {num2} es: {suma}")
print(f"{num1} / {num2} es: {division}")
print(f"{num1} * {num2} es: {multiplicacion}")
print(f"{num1} - {num2} es: {resta}")"

# Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es aproximadamente: {round(imc,2)}.")

# Ejercicio 9
celsius = float(input("Ingrese una temperatura en °C para convertirla en °F: "))
print(f"{celsius}°C equivale a {int(celsius*9/5 + 32)}°F")"

# Ejercicio 10
print("Voy a calcular el promedio de los 3 numeros que ingreses a continuacion: ")
num1, num2, num3 = int(input()), int(input()), int(input())
resultado = (num1+num2+num3) / 3
print(f"El promedio entre {num1}, {num2} y {num3} es: {int(resultado)}")"
