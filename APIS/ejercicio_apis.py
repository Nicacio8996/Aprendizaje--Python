"""
🧪 Reto — hazlo solo
Crea ejercicio_apis.py con un programa que:

Pregunte al usuario un país
Muestre la información del país
Pregunte si quiere consultar otro país
Si responde "si" → repita
Si responde "no" → se despida y termine
"""

import requests

while True:
    pais_buscar = input("¿Qué país quieres consultar? ")
    
    try:
        respuesta = requests.get(f"https://restcountries.com/v3.1/name/{pais_buscar}")
        if respuesta.status_code == 200:
            datos = respuesta.json()
            pais = datos[0]
            print("\n===== Información del país =====")
            print("Nombre oficial:", pais["name"]["official"])
            print("Capital:", pais["capital"][0])
            print("Población:", pais["population"])
            print("Región:", pais["region"])
        else:
            print("❌ País no encontrado")
    except:
        print("❌ Error de conexión")

    otro = input("\n¿Quieres consultar otro país? (si/no) ").lower()
    if otro == "no":
        print("¡Hasta luego!")
        break