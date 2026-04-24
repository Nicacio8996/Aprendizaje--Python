nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
ciudad = input("¿De dónde eres? ")

print("-------------------------------")
print("Resumen de tu información:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("-------------------------------")

"""
`input()` **siempre** devuelve texto aunque el usuario escriba números.
> Para convertirlo a número usamos `int()` — de la palabra *integer* (entero).
"""

#Este codigo da  este error
# File "C:\Users\ADRIANO\OneDrive - uniminuto.edu\Escritorio\Claude + Python\Python\leccion2.py", line 2, in <module>
   # años_en_10 = edad + 10
                 #~~~~~^~~~

"""                
#TypeError: can only concatenate str (not "int") to str
edad = input("¿Cuántos años tienes? ")
años_en_10 = edad + 10
print("En 10 años tendrás", años_en_10)
"""

#Para convertirlo a número usamos `int()` — de la palabra *integer* (entero).
edad = int(input("¿Cuántos años tienes? "))
años_en_10 = edad + 10
print("En 10 años tendrás", años_en_10, "años")