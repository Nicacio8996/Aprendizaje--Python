"""
suma = 0  # aquí guardamos la suma total
numero = " "    # aquí guardamos lo que escribe el usuario
while numero != "listo":
    numero = input("Escribe un numero ( o 'listo' para salir): ")  
    if numero != "listo":
        suma = suma + int(numero) # Aqui convertimos el numero en entero siempre y cuando el usuario ingrese un  nuemro.
print("La suma total es: ",suma)


# EXPLICACION DEL CODIGO:
#suma = 0      → empieza en 0 porque vamos a sumar
#numero = ""   → empieza vacío, el while lo llena


#**Anota por qué necesitamos el `if` adentro:**

Si el usuario escribe "listo"
no podemos convertirlo a número con int()
por eso verificamos primero
"""

suma = 0
numero_usuario =" "
while numero_usuario != "listo":
    numero_usuario = input("ingrese un numero (o 'listo' para salir): ")
    if numero_usuario != "listo":
        suma = suma + int(numero_usuario)
print("La suma es: ", suma)
