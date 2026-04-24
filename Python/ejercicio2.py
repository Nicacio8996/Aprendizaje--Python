nombre = input("Como te llamams? ")
precio = float(input("Cual es el precio del producto? "))
cantidad = int(input("Cua es la cantidad de productos que quieres conprar? "))
total_a_pagar = precio * cantidad
print("Hola", nombre, "el total de dinero que deves pagar por",cantidad,"unidades es:", total_a_pagar,"pesos")