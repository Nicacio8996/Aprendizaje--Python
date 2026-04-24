# Lección 5 - Listas
# Mi primera lista
"""
frutas = ["manzana", "pera", "mango", "banano"]

print(frutas)           # muestra toda la lista
print(frutas[0])        # muestra el primero
print(frutas[1])        # muestra el segundo
print(frutas[3])        # muestra el último
"""

"""
# Combinació de listas con for.
frutas = ["manzana", "pera", "mango", "banano"]
for fruta in frutas:
    print("Me gusta la ", fruta)
"""


frutas = ["manzana", "pera", "mango", "banano"]

# Agregar un elemento al final
frutas.append("uva")
print("Después de agregar:", frutas)

# Eliminar un elemento
frutas.remove("pera")
print("Después de eliminar:", frutas)

# Cuántos elementos tiene la lista
print("Total de frutas:", len(frutas))

"""
📓 **Anota en tu cuaderno:**

.append("x")  →  agrega "x" al final de la lista
.remove("x")  →  elimina "x" de la lista
len(lista)    →  cuenta cuántos elementos tiene
"""