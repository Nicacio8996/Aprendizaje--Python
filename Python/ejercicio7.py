producto = {
    "nombre": "aroz",
    "precio": 2400,
    "cantidad": 10,
    "categoria": "agranel"
}

for clave, valor in producto.items():
    print(clave,":", valor )

# Guarda el precio original primero:
precio_original = producto["precio"]

# Luego aplica el descuento:
producto["precio"] = producto["precio"] - producto["precio"] * 0.10

# Muestra los dos:
print("Precio original:", precio_original)
print("Precio con descuento:", producto["precio"])

#Modificar con 10% de descuento
#producto["precio"]= 2400 - 2400 * 0.10 
#print("nuevo precio con descuento ", producto["precio"])