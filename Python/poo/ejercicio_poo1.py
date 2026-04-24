class carro:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    def describir(self):
        print(f"Este es un carro marca, {self.marca}, modelo, {self.modelo}, del año, {self.año} y de color,{self.color} y esta a la venta.")

    def arranca(self):
        print(f"El carro maraca {self.marca}, esta arrancando.")

#Creando objeto
suzuki = carro("suzuki", "alto", 2022, "blanco")

#Llamando objeto
suzuki.describir()
suzuki.arranca()

#AGREGAR MAS OBJE8TOS
chevrolet = carro("Chevrolet", "spark", 2017, "rojo")
renault = carro("   Renault", "duster", 2023, "verde")
bmw = carro ("BMW", "especial", 2026, "azul")

print("====Nuevos objetos====")
chevrolet.describir()
renault.describir()
bmw.describir()

