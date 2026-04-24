"""
print("\n======Sin manejo de errores======")
# Sin manejo de errores — se rompe:
numero = int(input("Escribe un número: "))
print("El doble es:", numero * 2)
"""
"""
print("\n======Con manejo de errores======")
# Con manejo de errores — elegante:
try:
    numero = int(input("Escribe un número: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("❌ Error: debes escribir un número, no texto")

print("El programa continúa normalmente")
"""

"""
#Puedes manejar diferentes errores al mismo tiempo:
try:
    numero = int(input("Escribe un número: "))
    resultado = 10 / numero
    print("10 dividido entre", numero, "=", resultado)

except ValueError:
    print("❌ Error: eso no es un número")

except ZeroDivisionError:
    print("❌ Error: no se puede dividir entre cero")
"""

"""
try:
    numero = int(input("Escribe un número: "))
    resultado = 10 / numero
    print("10 dividido entre", numero, "=", resultado)

except ValueError:
    print("❌ Error: eso no es un número")

except ZeroDivisionError:
    print("❌ Error: no se puede dividir entre cero")
"""


try:
    numero = int(input("Escribe un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ValueError:
    print("❌ Error: eso no es un número")

except ZeroDivisionError:
    print("❌ Error: no se puede dividir entre cero")

finally:
    print("✅ Programa terminado correctamente")