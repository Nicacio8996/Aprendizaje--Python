# Lección 6 - Funciones
# Mi primera función
"""
def saludar(nombre):
    print("Hola", nombre, "bienvenido!")

saludar("Adriano")
saludar("Juan")
saludar("Maria")
"""


# Esta función DEVUELVE el resultado
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# Guardamos lo que devuelve
total = sumar(10, 5)
print("La suma es:", total)

# O usamos el resultado directo
print("Otra suma:", sumar(20, 30))

"""
📓 **Anota en tu cuaderno:**
```
return  →  devuelve un resultado
        →  la función "entrega" algo al final
"""