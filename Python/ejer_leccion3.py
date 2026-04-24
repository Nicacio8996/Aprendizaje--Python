nota = float(input("¿Cual es tu nota? "))

if nota >= 90:
    print("Eccelente")

elif nota >= 70 and nota< 90:
    print("Bueno")

elif nota >= 50 and nota < 70:
    print("Regular")

else:
    print("Reprobado")

#Mismo  codigo pero mas corto y eficiente:
nota = float(input("¿Cual es tu nota? "))

if nota >= 90:
    print("Excelente")

elif nota >= 70:
    print("Bueno")

elif nota >= 50:
    print("Regular")

else:
    print("Reprobado")