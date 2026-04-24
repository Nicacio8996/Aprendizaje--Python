# POO Clase 3 - Herencia

# Clase MADRE
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Clase HIJA - hereda de Animal
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Crear objetos
perro = Perro("Rex", 3)
gato = Gato("Michi", 2)

# El perro puede usar métodos de Animal Y los suyos
perro.comer()
perro.dormir()
perro.ladrar()

print("======================")
gato.comer()
gato.maullar()

print("==========================")
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # llama el __init__ de Animal
        self.raza = raza                # agrega atributo nuevo

    def ladrar(self):
        print(f"{self.nombre} ({self.raza}) dice: ¡Guau! y tiene {self.edad} años de edad")

    


# Crear objeto
perro = Perro("Rex", 3, "Labrador")
perro.comer()
perro.ladrar()

print("=========================")
class gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, color)
        self.color = color
        self.edad = edad
    def maullar(self):
        print(f"{self.nombre} de color {self.color} hace miau y tiene {self.edad} años de edad ")
#Crear objeto
gato = gato("Michi", 5, "Amarillo")
gato.comer()
gato.maullar()


print("===================")
class Pajaro(Animal):
    def __init__(self, nombre, edad, color, puede_volar):
        super().__init__(nombre, edad)
        self.color = color
        self.puede_volar = puede_volar

    def volar(self):
        if self.puede_volar:
            print(f"{self.nombre} de color {self.color} puede volar!")
        else:
            print(f"{self.nombre} de color {self.color} no puede volar")


# Crear objetos
pajaro1 = Pajaro("Pío", 1, "Verde", True)
pajaro2 = Pajaro("Pinguino", 3, "Negro", False)

pajaro1.comer()
pajaro1.volar()
pajaro2.volar()