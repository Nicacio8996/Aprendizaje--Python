import math # Importamos para poder hacer las operaciones.

#Función para el MCD
def obtener_MCM(a, b):
    # El MCM se calcula usando el Máximo Común Divisor (GCD)
    return abs(a * b) // math.gcd(a, b)

# Armamos la solucia o la función para la ecuacion cuadratica.
def resolver_cuadratica(a, b, c):
    # Cálculo del Vértice
    vx = -b / (2 * a)
    vy = a * (vx**2) + (b * vx) + c
    vertice = (vx, vy)

    # Cálculo de las Raíces
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "Sin solución real", vertice
    
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return (x1, x2), vertice

#Funcion menu con while True asate que se demuestre que no es verdadera.
def menu():
    while True:
        print("\n=== SÚPER CALCULADORA TecMD EN SERVICIO ===")
        print("1. Básicas (Suma, Resta, Multi, Div)")
        print("2. Potencia")
        print("3. Mínimo Común Múltiplo (MCM)")
        print("4. Ecuación Cuadrática")
        print("5. Salir")
        
        operacion = input("Elija una opción: ")
        
        if operacion == '5': break

        try: # Para manejo de errores.
            if operacion == '1':
                numero1 = float(input("Numero 1: "))
                numero2 = float(input("Numero 2: "))
                print("==== RESUMEN BASICAS ====")
                print(f"La suma es → {numero1 + numero2}")
                print(f"La resta es → {numero1 - numero2} ")
                print(f"La multiplicacion es → {numero1 * numero2}")

                if numero2 != 0: 
                    print(f"La divicion es → {numero1 / numero2}\n")
                else:
                    print("'¿Oye?, ¿Que Haces?  → No se puede dividir por cero lo ciento :(")
               
                    
               
                
            
            elif operacion == '2':
                base = float(input("Ingrese un numero Base para la potencia: → "))
                exponente = float(input("Exponente: "))
                print(f"RESUMEN → operacion expodencial: → {base} elevado a la {exponente} es → {base**exponente}")

            elif operacion == '3':
                a = int(input("Ingrese el Primer Número → "))
                b = int(input("Ingrese el Segundo número → "))
                print(f"Resumen: El MCM de → {a} y {b} es → {obtener_MCM(a, b)}")

            elif operacion == '4':
                print("\n==== RESUMEN ECUACIÓN CUADRÁTICA ====")
                print("Forma ax^2 + bx + c = 0")
                a = float(input("Ingrese 'a' Para tener en cuneta → si 'a', es negativa la parabola abre hacia abajo): → "))
                if a == 0:
                    print("Error: 'a' no puede ser cero en una cuadrática.")
                else:
                    b = float(input("Ingrese b: → "))
                    c = float(input("Ingrese c: →  "))
                    raices, vertice = resolver_cuadratica(a, b, c)
                    print(f"El Vértice se encuentra en el punto → {vertice}")
                    print(f"Las raíces son: → {raices}")
        
        except Exception as e:
            print(f"Error inesperado: {e}") # Pra errores apartes o inesperados sesun los datos ingresados.

menu() #Llamamos a la función menu