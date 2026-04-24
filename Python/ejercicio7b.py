#Agenda de contactos con un Diccionario.
agenda ={
    "adriano": 3101234567,
    "carmen": 3144445060,
    "maria": 3156446080,
    "juan": 3167608090
}
print("===Tus contactos son:===")
for clave, valor in agenda.items():
    print(clave, ":", valor)
nombre_contacto = input("¿Que contacto busca?🥰 ")
if nombre_contacto in agenda:
    print("El numero de",nombre_contacto.title(),  "es", agenda[nombre_contacto])

nombre_nuevo = input("Escribe el nombre del nuevo contacto: ")
numero_nuevo = input("Escribe el numero del nuevo contacto: ")
agenda [nombre_nuevo] = numero_nuevo
print(agenda)