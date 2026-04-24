"""
# Lección 4 - Bucles con for
# Imprime los números del 1 al 5

for numero in range(1, 6):
    print(numero)
    
for numero in range(1, 11):
    print(numero)

for numero in range(0, 10):
    print(numero)

for numero in range(1, 11):
    print("El numero es:",numero)
    """


#Ahora combinamos for con if
# Imprime solo los números pares del 1 al 10
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero, "es par")

    else:
        print(numero, "ES impar")