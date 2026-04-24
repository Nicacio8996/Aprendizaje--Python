#Iniciamos la clase madre Veiculo con sus metodos
class Veiculo:
    def __init__(self, marca, modelo, año): #Es el método constructor que se ejecuta al crear un objeto y se usa para inicializar sus atributos.
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def arranca(self):
        print(f"El {self.marca}, esta arrancando ")
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

#de aqui en adelante son clase hijas con metodos adicionales 
class Carro(Veiculo):
    def __init__(self, marca, modelo, año, puertas):
#super(). Permite llamar métodos de la clase padre, especialmente el constructor para inicializar atributos heredados.
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    def describir(self):
        print(f"Carrro {self.marca} de  {self.puertas} puertas ")

class Moto(Veiculo):
    def __init__(self, marca, modelo, año, cilindraje):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
    def describir(self):
        print(f"Moto {self.marca} de cilindraje {self.cilindraje}cc ")

class Camion(Veiculo):
    def __init__(self, marca, modelo, año, toneladas):
        super().__init__(marca, modelo, año)
        self.toneladas = toneladas
    def describir(self):
        print(f"Camion {self.marca} de {self.toneladas} toneladas  ")

print("========Menu========")
Veiculo = input("1. Agregue un veiculo: S/N ")
while Veiculo == "S":
    Veiculo = input("Ingrese la marca de su veiculo: ")
    Veiculo = input("Ingrese el modelo de su veiculo. ")
    Veiculo = input("Ingrese el año de su veiculo. ")


