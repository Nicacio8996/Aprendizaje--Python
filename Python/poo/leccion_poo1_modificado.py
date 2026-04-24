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
#RESUMEN
#¡Tres objetos, cada uno con sus propios datos, usando el mismo método! 💪
#RESULTADO:
"""
PS C:\Users\ADRIANO\OneDrive - uniminuto.edu\Escritorio\Claude + Python\Python\poo> python leccion_poo1_modificado.py
Hola, soy Adriano, tengo 37 años y vivo en Zipaquira
Hola, soy Juan, tengo 25 años y vivo en Bogotá
Hola, soy Maria, tengo 30 años y vivo en Medellín
PS C:\Users\ADRIANO\OneDrive - uniminuto.edu\Escritorio\Claude + Python\Python\poo>
"""