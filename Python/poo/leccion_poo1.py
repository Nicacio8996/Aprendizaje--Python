
# POO Clase 1 - Mi primera clase
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad


# Crear un objeto
adriano = Persona("Adriano", 37,"Zipaquira")

# Acceder a sus datos
print(adriano.nombre)
print(adriano.edad)
print(adriano.ciudad)


# Crear más objetos con la misma plantilla
juan = Persona("Juan", 25, "Bogotá")
maria = Persona("Maria", 30, "Medellín")

print("====Nuevos Agregados====")
print(juan.nombre, "tiene", juan.edad, "años")
print(maria.nombre, "vive en", maria.ciudad)

#RESULTADO
#¿Ves la magia? Una sola clase, tres objetos diferentes con sus propios datos. 💪


"""
PS C:\Users\ADRIANO\OneDrive - uniminuto.edu\Escritorio\Claude + Python\Python\poo> python leccion_poo1.py
Adriano
37
Zipaquira
====Nuevos Agregados====
Juan tiene 25 años
Maria vive en Medellín
PS C:\Users\ADRIANO\OneDrive - uniminuto.edu\Escritorio\Claude + Python\Python\poo>
"""


#Codigo anterior modificado😱
#AGREGAR UN METODO A LA CLASE.
#Un método es una función dentro de la clase. Modifica tu código así:
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}")

# Crear objetos
adriano = Persona("Adriano", 37, "Zipaquira")
juan = Persona("Juan", 25, "Bogotá")
maria = Persona("Maria", 30, "Medellín")

# Llamar el método
adriano.presentarse()
juan.presentarse()
maria.presentarse()

"""
📓 **Anota:**
```
método    →  función dentro de una clase
self      →  siempre va primero en los métodos
objeto.metodo()  →  así se llama el método
"""
