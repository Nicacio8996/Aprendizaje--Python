# Módulo math — operaciones matemáticas
import math

print(math.pi)                    # el número pi
print(math.sqrt(16))              # raíz cuadrada de 16
print(math.pow(2, 10))            # 2 elevado a la 10
print(math.ceil(4.3))             # redondea hacia arriba
print(math.floor(4.9))            # redondea hacia abajo

print("===================================")

import random

# Número aleatorio entre 1 y 10
print(random.randint(1, 10))

# Número decimal aleatorio entre 0 y 1
print(random.random())

# Elegir elemento aleatorio de una lista
frutas = ["manzana", "pera", "mango", "banano"]
print(random.choice(frutas))

# Mezclar una lista
random.shuffle(frutas)
print(frutas)

print("============================================")
print("\n====Modulo datetime====")
from datetime import datetime

# Fecha y hora actual
ahora = datetime.now()
print("Fecha y hora:", ahora)

# Solo partes específicas
print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)
print("Minutos:", ahora.minute)