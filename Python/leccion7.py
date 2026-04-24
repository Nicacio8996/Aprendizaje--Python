# Lección 7 - Diccionarios
"""
persona = {
    "nombre": "Adriano",
    "edad": 37,
    "ciudad": "Chía"
}
# Modificar un valor existente:
persona["edad"] = 38
print("Nueva edad ", persona["edad"])

# Agregar una clave nueva:
persona["profecion"] = "Desarrollador Python"
print("Profecion", persona["profecion"])

# Ver el diccionario completo:
print(persona)
"""


#🔍 Recorrer un diccionario con for
#Igual que las listas, puedes recorrer un diccionario automáticamente:
persona = {
    "nombre": "Adriano",
    "edad": 37,
    "ciudad": "Chía",
    "profesion": "Desarrollador Python"
}

for clave, valor in persona.items():
    print(clave, ":", valor)