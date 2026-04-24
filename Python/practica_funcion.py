"""
#Definir una funcion
def saludar(nombre): # solo la DEFINES
    print("Hola", nombre) # como guardar una receta
                            # pero no cocinar todavía
nombre_usuario = input("¿Cómo te llamas? ")
saludar(nombre_usuario)
"""


#Ahora viene el paso clave — las funciones con return. Modifica el código así:
def calcular_doble(numero):
    resultado = numero * 2
    return resultado

mi_numero = int(input("Escribe un número: "))
mi_doble = calcular_doble(mi_numero)
print("El doble es:", mi_doble)



# Estas 3 versiones hacen exactamente lo mismo:

# Versión 1:
mi_numero = int(input("Escribe un número: "))
mi_doble = calcular_doble(mi_numero)

# Versión 2:
numero = int(input("Escribe un número: "))
doble = calcular_doble(numero)

# Versión 3:
x = int(input("Escribe un número: "))
y = calcular_doble(x)

"""
Son variables normales — las inventas tú
para guardar el resultado de una función

resultado = calcular_doble(5)
   ↑
nombre que TÚ eliges para guardar
lo que devuelve la función
"""