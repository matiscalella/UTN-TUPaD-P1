# Trabajo practico 6 RECURSIVIDAD - Matias Scalella

# Ejercicio 1
# Imprimir todos los factoriales entre el 1 y un numero ingresado por el usuario.
def factorial(numero): # Definicion de la funcion recursiva para calcular el factorial
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
    
numero_limite = int(input("Ingrese un numero entero y positivo: ")) # Solicitud de ingreso de un numero

for i in range(1, numero_limite + 1): # Ciclo que recorre todos los numeros hasta el ingresado por el usuario
    print(f"{i}! = {factorial(i)}") # Impresion de cada numero en la secuencia y el calculo de su factorial utilizando la funcion recursiva

# Ejercicio 2
def secuencia_fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return secuencia_fibonacci(posicion-1)+secuencia_fibonacci(posicion-2)
# Secuencia para comprobacion: 0 1 1 2 3 5 8 13 21 34 ...
                                
print("-- Visualizador de la secuencia de Fibonacci (0 1 1 2 3 5 8 13 21 34 ...) --")
posicion_usuario = int(input("Ingrese la posicion de la secuencia: "))

for i in range(0, posicion_usuario + 1):
    print(f"Posicion: {i}, Valor de Fibonacci: {secuencia_fibonacci(i)}")

# Ejercicio 3
# Caso base: exponente = 0
# Paso recursivo: base * funcion(base, exponente - 1) 
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Caso de uso    
num_base = int(input("Ingrese la base: "))
num_exponente = int(input("Ingrese la potencia: "))

# Ejercicio 4
# Case base: numero == 0
# Paso recursivo: numero // 2 y numero % 2

def decimal_a_binario(numero):
    if numero == 0:
        return "" # Cuando el numero ingresado llega a cero, la funcion devuelva un string vacio.
    else: 
        return decimal_a_binario(numero // 2) + str(numero % 2) # numero // 2 devuelve la parte entera, y numero % 2 concatena 0 o 1 con cada vuelta
    
print(decimal_a_binario(8))
# Secuencia para seguir la funcion recursiva:
# decimal_a_binario(8) devuelve decimal_a_binario(4) + "0" -> (8 % 2 = 0)
# decimal_a_binario(4) devuelve decimal_a_binario(2) + "0" -> (4 % 2 = 0)
# decimal_a_binario(2) devuelve decimal_a_binario(1) + "0" -> (2 % 2 = 0)
# decimal_a_binario(1) devuelve decimal_a_binario(0) + "1" -> (1 % 2 = 1)
# decimal_a_binario(0) alcanza el caso base y devuelve "" un string vacio
# Al desapilarse, la impresion es 1000 con lo cual no es necesario invertir los restos como si utilizaramos bucles