"""
suma_intentos = 0
numero_secreto = 27
usuario_numero = " "
while usuario_numero != 27:
    usuario_numero = int(input("Adivina el numero:('pista' el numero es un entero: )"))
    if usuario_numero > 27:
        print("El numero que te toca adivinar es menor a tu ", usuario_numero)
    if usuario_numero < 27:
        print("El numero que te toca adivinar es mayor a tu: ",usuario_numero)
    suma_intentos = suma_intentos +1
print("Lo adivinaste en ",suma_intentos, "intentos")

"""
# CODIGO ANTERIOR CORREGIDO:
suma_intentos = 0
numero_secreto = 27
usuario_numero = " "
while usuario_numero != numero_secreto:
    usuario_numero = int(input("Adivina el numero ( 'pista:' el numero es un entero): "))
    suma_intentos = suma_intentos + 1
    if usuario_numero > numero_secreto:
        print("El numero que te toca adivinar es menor a tu: ",usuario_numero)
    elif usuario_numero < numero_secreto:
        print("El numero que te toca adivinar es mayor a tu:",usuario_numero)
    else:
        print("Adivinaste en ",suma_intentos)
