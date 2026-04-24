lista_nombres = ["Adriano", "eva", "martha", "maria", "carlos"]
print(lista_nombres)

print("En total hay: ",len(lista_nombres), "personas")

for nombre in lista_nombres:
    print("Hola", nombre.title(),"bienvenido!")

lista_nombres.append("mario")
print("Y, la lista final es: ",lista_nombres)