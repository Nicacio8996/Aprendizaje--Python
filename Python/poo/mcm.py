def gcd(a ,b):
    while b:
        a, b = b, a% b
    return a
def lcm(a, b):
    return(a * b) // gcd(a, b)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

lcm_result = lcm(num1, num2)

print(f"El minimo comun multiplo de {num1} y {num2} es {lcm_result}. ")

