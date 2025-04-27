## LISTAS
# Matias Scalella - Comision 21
# Ejercicio 1
lista_de_numeros = list(range(4,101,4))
print(lista_de_numeros)

# Ejercicio 2
lista_favoritos = ["Libros", "Programar", 13, "Mate", "Musica"]
print(lista_favoritos[len(lista_favoritos)-2]) # tambien se puede acceder sabiendo que son 5 elementos, usando lista_favoritos[3]

# Ejercicio 3
lista_vacia = []
lista_vacia.append(13)
lista_vacia.append(True)
lista_vacia.append("Bateria")
print(lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] =  "loro"
animales[-1] = "oso"
print(animales)

# Ejercicio 5
numeros = [8, 15, 3, 22, 7] # Esta linea crea una lista con valores que son numeros enteros, desordenados
numeros.remove(max(numeros)) # Esta linea elimina el mayor de los elementos de la lista. Primero lo busca y luego lo elimina.
print(numeros) # Esta linea imprime la lista de numeros actualizada, con el mayor de los numeros eliminado.

# Ejercicio 6
numeros_10al30 = list(range(10, 31, 5))
print(numeros_10al30[0:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "yaris"
autos[2] = "fox"
print(autos)

# Ejercicio 8
dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)