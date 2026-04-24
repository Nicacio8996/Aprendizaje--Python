nombre = input("Ingresa tu nombre ")
valor_compra = float(input("Ingresa el valor de tu compra "))

if valor_compra >= 200000:
    descuento = valor_compra * 0.20
    total = valor_compra - descuento
    print("Hola", nombre,"el total de tu compra con eldescuento es",total,"pesos")
    print("Ahorraste", descuento, "pesos")

elif valor_compra >= 100000:
    descuento = valor_compra * 0.10
    total = valor_compra - descuento
    print("Hola", nombre, "el total de tu compra con eldescuento es",total,"pesos")
    print("Ahorraste", descuento, "pesos")

elif valor_compra >= 50000:
    descuento = valor_compra * 0.05
    total = valor_compra - descuento
    print("Hola", nombre,"el total de tu compra con descuento es", total,"pesos")
    print("Ahorraste", descuento, "pesos")

else:
    print("Hola",nombre, "su compra es de",valor_compra,"pesos sin descuento ")
   