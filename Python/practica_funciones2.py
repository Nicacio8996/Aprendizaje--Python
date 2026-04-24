def calcular_propina (total_cuenta, porcentaje_propina):
    total_propina = total_cuenta * porcentaje_propina / 100
    return total_propina

def mostrar_cuenta(valor_inicial, total_propina):
    total= valor_inicial + total_propina
    return total


nombre = input("Ingresa su nombre ")
valor_inicial = float(input("Ingresa el lalor inicial de la cuenta "))
propina = float(input("Ingresa el porsentaje de la propina, ejemplo 20: "))

mi_propina = calcular_propina(valor_inicial, propina)
print("Hola ", nombre, "tu total con propina es ",mostrar_cuenta(valor_inicial, mi_propina))


    









    
