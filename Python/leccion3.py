# Lección 3 - Condicionales
# El programa decide si eres mayor o menor de edad

# Lección 3 - Condicionales con elif
# Clasificador de edades

edad = int(input("¿Cuántos años tienes? "))

if edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


