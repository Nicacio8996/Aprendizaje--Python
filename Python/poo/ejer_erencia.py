"""
🧪 Ejercicio — Sistema de empleados
Crea una clase madre Empleado con:

Atributos: nombre, salario
Métodos:
  trabajar()  → "Adriano está trabajando"
  mostrar_info() → "Nombre: Adriano, Salario: $2000000"

  Crea 2 clases hijas:
Vendedor hereda de Empleado:

Atributo extra: comision
Método: vender() → "Adriano vendió y ganó $200000 de comisión"

Programador hereda de Empleado:

Atributo extra: lenguaje
Método: programar() → "Adriano está programando en Python"

Crea 2 objetos de cada clase y prueba todos los métodos.
"""

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def trabaja(self):
        print(f"{self.nombre} esta trabajando ")
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, salario: {self.salario}")
    
class Vendedor(Empleado):
    def __init__(self, nombre, salario, comicion):
        super().__init__(nombre, salario)
        self.comicion = comicion
    def vende(self):
        self.total = self.salario + self.comicion
        print(f"{self.nombre} tiene un salario de  {self.salario} mas una comision de {self.comicion} par aun total de {self.total} de sueldo o salario ")
        

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
    def programar(self):
        print(f"{self.nombre} esta programando en lenguaje {self.lenguaje} ")

# CREAR DOS OBJETOS
persona1 =  Empleado("Adriano", 2000000)
persona2 = Vendedor("Adriano Figueroa", 200000, 100000)
persona3 = Programador("Adriano Figueroa", 200000, "Python")

# PROBAR LOS MÉTODOS
persona1.trabaja()
persona1.mostrar_info()



persona2.vende()
persona3.programar()






