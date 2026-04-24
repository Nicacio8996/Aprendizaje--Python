try:
    numero1 = int(input("Ingrese un numero: \n"))
    numero2 = int(input("Ingrese otro numero: \n"))
    resultado = numero1 + numero2
    print("La suma es : ", numero1, "+", numero2, "=", resultado)
    resultado1 = numero1 * numero2
    print("La multiplicacion es: ", numero1, "*" , numero2, "=", resultado1)
    resultado2 = numero1 - numero2
    print("La resta es: ", numero1, "-", numero2, "=", resultado2)
    resultado3 = numero1 / numero2
    print("La divición es.", numero1, "/", numero2, "=",
           resultado3)
except ValueError:
    print("Ingrese numeros no letras: ")

except ZeroDivisionError:
    print("No se puede dividir por cero: ")

finally:
    print("Operaciones terminadas: ")
    