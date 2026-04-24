with open("contacto.txt", "w", encoding="utf-8") as archivo: 
    nombre = input("¿Cual es tu nombre? ").title()
    edad = input("¿Cual es tu edad? ")
    ciudad = input("¿Cual es tu ciudad? ").title()
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad:  {edad} años\n")
    archivo.write(f"Ciudad: {ciudad}\n")
with open("contacto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("\nDatos guardados exixtosamente")
    print("\n===Tus datos son===")
    print(contenido)
guardar_otro_dato = input("¿Desea agregar tu profeción? (s/n) ").lower()
if guardar_otro_dato == "s":
    profecion = input("¿Cual es tu profeción? ").title()
    with open("contacto.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Profecion: {profecion}")
else:
    print("Ok, no te interesa guardar tu profecion")
#print(contenido)

# para mostras los archivos al final
with open("contacto.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())

    
   
