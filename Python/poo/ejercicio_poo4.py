class Figura:
    def __init__(self, area):
        self.area = area 

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
      
    
    def calcular_area(self):
        self.area = self.lado * self.lado
        print(f"Cuadrado : el araea es {self.area}")

class Rectangulo(Figura):
    def  __init__(self,  base , altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        self.area = self.base * self.altura
        print(f"Rectangulo: el area es {self.area}")

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        self.area = self.base * self.altura / 2
        print(f"Triangulo: el arae es {self.area}")
  
figuras = [Cuadrado(4), Rectangulo(6, 8), Triangulo(10, 5)]

for figura in figuras:
   figura.calcular_area()


#resultado:
"""
Cuadrado : el araea es 16
Rectangulo: el area es 48
Triangulo: el arae es 25.0
"""
#RESUMEN:
"""
POO Clase 4 - Polimorfismo:

Mismo método → comportamientos diferentes
según el objeto que lo llame

class Hija1(Madre):
    def metodo(self):  → hace X

class Hija2(Madre):
    def metodo(self):  → hace Y

for objeto in lista:
    objeto.metodo()   → cada uno hace lo suyo
"""
