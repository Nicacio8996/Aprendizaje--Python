"""
import requests

# Hacemos una petición a la API
respuesta = requests.get("https://restcountries.com/v3.1/name/colombia")

# Verificamos que funcionó
print("Estado:", respuesta.status_code)
print("Tipo de datos:", type(respuesta.json()))
"""

"""
import requests

respuesta = requests.get("https://restcountries.com/v3.1/name/colombia")
datos = respuesta.json()

# Los datos del primer resultado
pais = datos[0]

print("Nombre oficial:", pais["name"]["official"])
print("Capital:", pais["capital"][0])
print("Población:", pais["population"])
print("Región:", pais["region"])
print("Moneda:", list(pais["currencies"].keys())[0])
"""



#🔍 Ahora hagámoslo interactivo
import requests

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

except Exception as e:
    print("❌ Error de conexión:", e)

