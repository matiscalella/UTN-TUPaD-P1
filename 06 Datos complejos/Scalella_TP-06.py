## Trabajo practico 6 Estructuras de datos complejas
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

# Ejercicio 4 - Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar.
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    def saludar(self):
        print(f"Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
        
persona1 = Persona("Matias", "Argentina", 34)

persona1.saludar()

# Ejercicio 5 - Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro.
from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * pi * self.radio

radio_del_circulo1 = Circulo(6)
print(f"El area del circulo es: {radio_del_circulo1.calcular_area():.2f}")
print(f"El perimetro del circulo es: {round(radio_del_circulo1.calcular_perimetro(), 2)}")

# Ejercicio 6 - Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.

