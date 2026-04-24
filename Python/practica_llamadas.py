def calular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio
    

def mostrar_resultado(nombre, promedio):
    print("====Miremos el promedio====")
    if promedio >= 60:  # ← adentro de la función
        print("Hola", nombre, "tu promedio es ", promedio, "Aprobaste")
    else:
        print("Hola", nombre, "Tu promedio es ", promedio, "reprobaste")


nombre = input("Ingrese su nombre ")
nota1 = float(input("Ingrese la nota1: "))
nota2 = float(input("Ingrese la nota2: "))
nota3 = float(input("Ingrese la nota3: "))

mi_promedio = calular_promedio(nota1, nota2, nota3)
mostrar_resultado(nombre, mi_promedio)




