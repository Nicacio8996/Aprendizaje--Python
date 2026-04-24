# POO Clase 4 - Polimorfismo

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Sonido genérico")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

class Pajaro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Pío!")

#Puedes guardar objetos dentro de una lista
#y recorrerlos con for — eso es muy poderoso!
# La magia del polimorfismo:
animales = [Perro("Rex"), Gato("Michi"), Pajaro("Pío")]

for animal in animales:
    animal.hablar()