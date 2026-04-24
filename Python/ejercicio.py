# Lección 2 - input() e int()
# Programa que calcula en qué año cumples 100 años:

# Pedimos el nombre del usuario
nombre = input("Escribe tu nombre ")
# Pedimos el año de nacimiento y lo convertimos a número con int()
año_nacimiento = int(input("Ingrese tu año de nacimiento "))
# Calculamos el año en que cumplirá 100 años
años_en_100 = año_nacimiento + 100
# Mostramos el resultado
print("Hola", nombre, "usted cumplira 100 años en", años_en_100)
