## Ejercicio 1
# Funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa Principal
imprimir_hola_mundo()

## Ejercicio 2
# Funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa Principal
nombre = input("Bienvenido, ingresa tu nombre: ")
saludar_usuario(nombre)

## Ejercicio 3
# Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa Principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

## Ejercicio 4
# Funciones
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa Principal
radio = float(input("Hola, ingresa el radio del circulo: "))
area = round(calcular_area_circulo(radio), 2)
perimetro = round(calcular_perimetro_circulo(radio), 2)
print(f"El area del circulo es {area}")
print(f"El perimetro del circulo es {perimetro}")

## Ejercicio 5
# Funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return round(horas, 2)

# Programa Principal
segundos_usuario = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos_usuario} equivale a {segundos_a_horas(segundos_usuario)} horas.")

## Ejercicio 6
# Funciones
def es_natural(mensaje, min = float("-Inf"), max = float("Inf")): # Funcion para determinar la validez del numero ingresado
    num = int(input(mensaje))
    while num < min or num > max:
        num = int(input(f"ERROR! {mensaje}"))
    return num

def tabla_multiplicar(numero):
    tabla = ""
    for i in range (1, 11):
        tabla += f"{numero} x {i}: {i*numero}\n"
    return tabla

# Programa Principal
numero = es_natural("Ingrese un numero natural positivo para conocer su tabla de multiplicar: ", 1)
print(f"Tabla de multiplicar del {numero}:")
print(tabla_multiplicar(numero))


## Ejercicio 7
# Funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

def validar_numero(mensaje, min = float("-Inf"), max = float("Inf")): # Funcion para determinar la validez del numero ingresado
    num = float(input(mensaje))
    while num < min or num > max:
        num = float(input(f"ERROR! {mensaje}"))
    return num

def validar_numero_distinto_a_cero(mensaje, min = float("-Inf"), max = float("Inf")): # Funcion para determinar la validez del numero ingresado que no puede ser cero
    num = float(input(mensaje))
    while num == 0:
        num = float(input(f"ERROR! {mensaje}"))
    return num

# Programa Principal
a = validar_numero("Ingresa un numero: ")
b = validar_numero_distinto_a_cero("Ingresa un numero distinto de 0 (cero): ")
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicacion: {a} * {b} = {multiplicacion}")
print(f"Division: {a} / {b} = {round(division, 2)}")

## Ejercicio 8
# Funciones
def calcular_imc(peso, altura):
    return peso / (altura**2)

def validar_numero(mensaje): # Validacion los valores ingresados por el usuario
    numero = float(input(mensaje))
    while numero <= 0:
        numero = float(input(f"Error, entrada invalida. {mensaje}"))
    return numero

# Programa Principal
kilogramos = validar_numero("Ingrese su peso: ")
metros = validar_numero("Ingrese su altura: ")
print(f"Usted pesa {kilogramos} kgs. y mide {metros} mts.")
imc = calcular_imc(kilogramos, metros)
print(f"Su IMC es: {imc:.2f}") # redondeo del IMC, tambien se puede hacer con {round(imc, 2)}

## Ejercicio 9
# Funciones
def validar_grados_Celsius(mensaje, min = float("-Inf"), max = float("Inf")): # Validacion de grados celsius ingresados por el usuario
    temperatura = float(input(mensaje))
    while temperatura < min or temperatura > max:
        temperatura = float(input(f"ERROR. Ingreso un valor menor la temperatura minima teorica.\n{mensaje}"))
    return temperatura

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa Principal
celsius = validar_grados_Celsius("Ingrese la temperatura en °C: ", -273.15)
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius:.2f} °C equivale a: {fahrenheit:.2f} °F.")

## Ejercicio 10
# Funciones
def validar_numero(mensaje): # Funcion para validar que el usuario ingrese unicamente numeros
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("ERROR. Ingreso inválido. Debe ser un número.")

def calcular_promedio(a, b, c):
    return (a + b+ c) / 3

# Programa Principal
print("Hola, calculo el promedio de 3 numeros que ingreses: ")
num1 = validar_numero("Ingresa el primer numero: ")
print("Primer numero validado, podes ingresar el segundo.")
num2 = validar_numero("Ingresa el segundo numero: ")
print("Segundo numero validado, podes ingresar el tercero.")
num3 = validar_numero("Ingresa el tercer numero: ")
print("Validacion de numeros OK.")
print("\n--- RESULTADO ---")
print(f"Calculo el promedio de {num1}, {num2} y {num3}.")
print(f"Promedio: {calcular_promedio(num1, num2, num3):.2f}")
