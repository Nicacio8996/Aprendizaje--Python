# Lección 9 - Bucle while
# Cuenta del 1 al 5
"""
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1

print("¡Terminé de contar!")

"""
"""
contador = 1          → empezamos en 1
while contador <= 5:  → mientras sea menor o igual a 5
    print(contador)   → muestra el número
    contador += 1     → suma 1 cada vez
                        SIN ESTO el programa nunca para ⚠️


#SIN EL CONTADOR += 1 SE CONBIENRTE EN UN BUCLE INFINITO
contador = 1
while contador <= 5:
    print(contador)
"""


# El programa no para hasta que el usuario escriba "salir"
#!=  →  diferente a
#while respuesta != "salir"
# → repite MIENTRAS la respuesta sea diferente a "salir"
respuesta = ""

while respuesta != "salir":
    respuesta = input("Escribe algo (o 'salir' para terminar): ").lower()
    print("Escribiste:", respuesta)

print("¡Hasta luego!")