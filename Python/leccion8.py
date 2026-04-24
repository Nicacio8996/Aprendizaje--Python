# Lección 8 - Archivos
# Escribir en un archivo

archivo = open("mis_datos.txt", "w", encoding="utf-8")
archivo.write("Hola, soy Adriano\n")
archivo.write("Estoy aprendiendo Python\n")
archivo.write("Desde Chía, Colombia\n")
archivo.close()

print("Archivo guardado exitosamente!")

"""
📓 **Anota:**
open()         → abre o crea el archivo
archivo.write() → escribe en el archivo
archivo.close() → cierra el archivo (importante!)
\n             → salto de línea
"""

"""
# Leer el archivo
archivo = open("mis_datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()
print("=== Contenido del archivo ===")
print(contenido)
"""


# Los profesionales usan para leer el archiov mas limpio y seguro
with open("mis_datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)





# Agregar más información sin borrar lo anterior
archivo = open("mis_datos.txt", "a", encoding="utf-8")
archivo.write("Mi meta es conseguir trabajo remoto\n")
archivo.close()

print("Línea agregada!")

# Leer todo el archivo
archivo = open("mis_datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()

print("=== Contenido completo ===")
print(contenido)
"""
📓 **Anota en tu cuaderno:**
"w" → borra todo y escribe desde cero
"a" → agrega al final sin borrar nada
"""


