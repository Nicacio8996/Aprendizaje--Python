"""
random — cree un juego donde:

Python piensa un número entre 1 y 20
El usuario tiene 3 intentos para adivinarlo
Al final muestre si ganó o perdió
"""


"""
print("======Juego random======")

import random
numero_secreto = random.randint(1, 20)
intentos = 3

while intentos > 0:
    
        usuario_numero = int(input("Ingrese un numero entero entre 1 y 20: "))
        
        if usuario_numero == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Incorrecto. Te quedan {intentos} intentos.")
            else:
                print(f"Perdiste. El número secreto era {numero_secreto}.")
    
"""
print("Fin del juego.")

print("\n::::::::::::::::::::::::::::::::::::::::")
import math
numro = float(input("Ingrese un numero "))
print(math.sqrt(numro))
print("\n:::::::::::::::::::::::::::::::::::")
from datetime import datetime
saludar = datetime.now()
saludo = saludar.hour
if saludo >= 5 and saludo < 12:
    print("¡Buenos días!")
elif saludo >= 12 and saludo <= 18:
    print("¡Buenas tardes!")
else:
    print("¡Buenas noches!")


       
import random
numero_secreto = random.randint(1, 20)
intentos = 3

while intentos > 0:
    usuario_numero = int(input(f"Adivina (tienes {intentos} intentos): "))
    if usuario_numero == numero_secreto:
        print("¡Ganaste!")
        break
    elif usuario_numero < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    intentos -= 1

if intentos == 0:
    print(f"¡Perdiste! El número era {numero_secreto}")   

    
        
    






