def descuento (precio, porcentaje):
    resultado = precio * porcentaje / 100
    return resultado


def calcular_total (precio, descuento):
    total_pagar = precio - descuento
    return total_pagar



def mostrar_resumen(nombre, precio, descuento, total_pagar):
    print("========Resumen de compra==========")
    print("Hola ", nombre)
    print("El precio del producto es", precio)
    print("El descuento es de ", descuento)
    print("total a pagar es",total_pagar )

# 2️⃣ DESPUÉS - usas las funciones
nombre = input("ingrese su nombre ")
precio = float(input("Ingrese el precio "))
porcentaje = float(input("ingrese el porcentaje de descuento "))

mi_descuento = descuento(precio, porcentaje)
mi_total = calcular_total(precio, mi_descuento)
mostrar_resumen (nombre, precio,mi_descuento,mi_total)




