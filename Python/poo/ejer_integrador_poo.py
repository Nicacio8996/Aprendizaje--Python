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

 #Crear objeto
carro = Carro("Toyota", "Famiy", 2026, 4)
#print(f"Este es un {carro.marca} modelo {carro.modelo} del  año {carro.año} de {carro.puertas} puertas ")
carro.arranca()
carro.mostrar_info()

#Creando lista para quetrabaje el polimorfismo
veiculos = [
    Carro("Toyota", "Family", 2026, 4), 
    Moto("Kawasaki", "Ninja H2R", 2026, 998), 
    Camion("Kenworth", "T1200", 2024, 45)
]
#Este codigo sirve para recorrer la lista
# Polimorfismo: cada vehículo llama su propio describir()
for veiculo in veiculos:
    veiculo.describir()