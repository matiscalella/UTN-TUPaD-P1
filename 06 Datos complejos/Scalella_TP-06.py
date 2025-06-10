## Trabajo practico 6 Estructuras de datos complejas SIN OBJETOS
# Ejercicio 1 - Agregar elementos nuevos al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200 
precios_frutas['Manzana'] = 1500 
precios_frutas['Pera'] = 2300

print(precios_frutas) # {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# Ejercicio 2 Modificar valores del diccionario
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas) # {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# Ejercicio 3 Crear una lista que contenga unicamente los nombres de las frutas, sin los precios
nombres_de_frutas = list(precios_frutas.keys())
print(nombres_de_frutas) # ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']

# Ejercicio 4 - Escribí un programa que permita almacenar y consultar números telefónicos
print("Hola vamos a cargar 5 nombres y telefonos para crear una agenda.")
agenda = {}

for i in range(1, 6):
    contacto = input(f"Ingrese el nombre de tu contacto numero {i}: ")
    telefono = input(f"Ingresa el numero asociado para {contacto}: ")
    agenda[contacto] = telefono

print("Tu agenda ha sido creada.")
nombre_de_contacto = input("Ingresa alguno de los nombres de tus contactos para verificar su numero: ")
if nombre_de_contacto in agenda:
    print(f"Tengo asociado para {nombre_de_contacto} el telefono: {agenda[nombre_de_contacto]}")
else:
    print("Ese contacto no se encuentra en la agenda.")

# Ejercicio 5 - Solicitar al usuario una frase e imprimir las palabras unicas y un diccionario con la cant. de veces que aparece cada palabra.
frase_usuario = input("Ingresá una frase: ")

palabras = frase_usuario.split() # Separo la frase en palabras.

palabras_unicas = set(palabras) # Creo un set con las palabras (no hay repetidas)
print("\nPalabras únicas:")
print(palabras_unicas)

frecuencias = {} # Creo el diccionario que contara las palabras

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencias.items():
    print(f"{palabra}: {cantidad}")

# Ejercicio 6 - Cargar 3 alumnos, y crear para cada uno una tupla con 3 notas. Imprimir el promedio de cada alumno al final
alumnos = {}

for i in range(1, 4): # Cargar 3 alumnos con sus 3 notas (tupla)
    nombre = input(f"Ingresá el nombre del alumno {i}: ")
    notas = []

    for j in range(1, 4):
        nota = float(input(f"Ingresá la nota {j} de {nombre}: "))
        notas.append(nota)

    alumnos[nombre] = tuple(notas)  # Guardar como tupla

print("\nPromedios de cada alumno:")# Mostrar promedios
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Ejercicio 7 - Operaciones con sets
parcial1 = {"Brian", "Jorge", "Matias", "Juan", "Licha"}
parcial2 = {"Licha", "Matias", "Valentina", "Carlos", "Elena"} 

aprobaron_ambos = parcial1 & parcial2
print(f"Los que aprobaron ambos parciales son: {aprobaron_ambos}")

aprobaron_uno_solo = parcial1 ^ parcial2
print(f"Los que aprobaron solo uno de los parciales son: {aprobaron_uno_solo}")

aprobaron_al_menos_uno = parcial1 | parcial2
print(f"Los que aprobaron al menos uno de los parciales son: {aprobaron_al_menos_uno}")

# Ejercicio 8
# Diccionario inicial con productos y su stock
stock_productos = {"manzanas": 15, "bananas": 10,"peras": 6}

producto = input("Ingresá el nombre de un producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades.")

    # Agregar más unidades
    agregar = int(input(f"¿Cuántas unidades querés agregar a {producto}? "))
    stock_productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades.")
else:
    # Agregar nuevo producto
    nuevo_stock = int(input(f"{producto} no está en el inventario. ¿Cuántas unidades querés agregar? "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} fue agregado al inventario con {nuevo_stock} unidades.")

# Mostrar stock actualizado
print("\nStock actualizado:")
for prod, cant in stock_productos.items():
    print(f"{prod}: {cant} unidades")

# Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Desayuno familiar",
    ("martes", "14:00"): "Parcial de Programacion",
    ("miércoles", "09:00"): "Reunion de trabajo",
    ("viernes", "18:30"): "Gimnasio"
}

# Solicitar al usuario dia y hora para consultar
dia = input("Ingresá el dia para consultar (por ejemplo: lunes): ").lower()
hora = input("Ingresá la hora (ej: 14:00): ")

clave = (dia, hora)

if clave in agenda: # Verificar si hay evento en ese momento
    print(f"El evento agendado el {dia} a las {hora} es: {agenda[clave]}")
else:
    print(f"No hay ningún evento agendado el {dia} a las {hora}.")

# Ejercicio 10
paises_a_capitales = {"Argentina": "Buenos Aires","Francia": "París","Brasil": "Brasilia","Italia": "Roma","Japón": "Tokio"}

capitales_a_paises = {} # Nuevo diccionario

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital ahora es pais):")
for capital, pais in capitales_a_paises.items():
    print(f"{capital}: {pais}")