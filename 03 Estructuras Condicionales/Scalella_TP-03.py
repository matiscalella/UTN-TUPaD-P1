# TP3 Matias Scalella - Correr las tres comillas para verificar uno o uno los ejercicios
# Ejercicio 1 

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
if string[-1].lower() in ["a", "e", "i", "o", "u"]: #los corchetes en valor [-1] toman el ultimo caracter porque cuentan desde el final de la cadena y lo transforma en minuscula para compararlo con la lista de vocales
    print(string + "!")
else:
    print(string)

# Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("Seleccione 1, 2 o 3:")
print("1. Si quiere su nombre en MAYUSCULAS.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input("Opcion elegida: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingreso una opcion incorrecta, ejecute el programa nuevamente.")
    pass

# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto para conocer su clasificacion segun la escala de Richter: "))
clasificacion = ""
if magnitud < 3:
    clasificacion = "Muy leve"
elif 3 <= magnitud < 4:
    clasificacion = "Leve"
elif 4 <= magnitud < 5:
    clasificacion = "Moderado"
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte"
elif 6 <= magnitud < 7:
    clasificacion = "Muy Fuerte"
elif magnitud >= 7:
    clasificacion = "Extremo"

print(f"Clasificacion del terremoto: {clasificacion.upper()}")


# Ejercicio 10
from datetime import date #modulo para trabajar con fechas

print("Hola voy a decirte en que estacion del año te encontras, en funcion del hemisferio en el que te encontras, dia y mes actuales (para el 2025). ")
print("¿En que hemisferio te encontras? ¿Norte o Sur?")
hemisferio = input("Responde N o S: ").lower()
mes = int(input("¿Que mes del año es hoy? (1-12): "))
dia = int(input("¿Que dia del mes? (1-31): "))
fecha = date(2000, mes, dia)
estacion = ""

if hemisferio == "n":
    inicio_invierno_norte = date(2000, 12, 21)
    fin_invierno_norte = date(2000, 3, 20)
    inicio_primavera_norte = date(2000, 3, 21)
    fin_primavera_norte = date(2000, 6, 20)
    inicio_verano_norte = date(2000, 6, 21)
    fin_verano_norte = date(2000, 9, 20)
    inicio_otono_norte = date(2000, 9, 21)
    fin_otono_norte = date(2000, 12, 20)

    if inicio_invierno_norte <= fecha <= fin_invierno_norte: 
        estacion = "Invierno"
    elif inicio_primavera_norte <= fecha <= fin_primavera_norte:
        estacion = "Primavera"
    elif (date(2000, 1, 1) <= fecha <= date(2000, 3, 20)) or (date(2000, 12, 21) <= fecha <= date(2000, 12, 31)):
        estacion = "Verano"
    elif inicio_otono_norte <= fecha <= fin_otono_norte:
        estacion = "Otoño"

elif hemisferio == "s":
    inicio_invierno_sur = date(2000, 6, 21)
    fin_invierno_sur = date(2000, 9, 20)
    inicio_primavera_sur = date(2000, 9, 21)
    fin_primavera_sur = date(2000, 12, 20)
    inicio_verano_sur = date(2000, 12, 21)
    fin_verano_sur = date(2000, 3, 20)
    inicio_otono_sur = date(2000, 3, 21)
    fin_otono_sur = date(2000, 6, 20)

    if inicio_invierno_sur <= fecha <= fin_invierno_sur:
        estacion = "Invierno"
    elif inicio_primavera_sur <= fecha <= fin_primavera_sur:
        estacion = "Primavera"
    elif (date(2000, 1, 1) <= fecha <= date(2000, 3, 20)) or (date(2000, 12, 21) <= fecha <= date(2000, 12, 31)):
        estacion = "Verano"
    elif inicio_otono_sur <= fecha <= fin_otono_sur:
        estacion = "Otoño"
else:
    print("Ingresaste una opcion no valida, reinicia el programa.")

print(f"En el hemisferio {'Norte' if hemisferio == 'n' else 'Sur'} estas en: {estacion}")