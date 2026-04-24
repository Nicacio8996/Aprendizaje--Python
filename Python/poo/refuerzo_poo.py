class productos:
    def __init__(self, nonbre, precio, cantidad):
        self.nonbre = nonbre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"El producto, {self.nonbre} tiene un precio de, {self.precio} y tenemos una cantidad de, {self.cantidad} 'Bienvenodo' ")
    
    def vender(self,cantidad):
        if cantidad > self.cantidad:
             print("Lo sentimos no tenemos sufuciente producto ")
        else:
             self.cantidad -= cantidad
             print(f"Vendido Stok restante: {self.cantidad}")

    def  aplicar_descuento(self, porcentaje):
         descuento = self.precio * porcentaje / 100
         self.precio = self.precio - descuento 
         print(f" Nuevo precio con descuento es {self.precio} pesos")

    
 
    
#creamos los ohbjetos
arroz = productos("Arroz", 1200, 100)
televisor = productos("Lg 11''", 2000000, 4)

#Llamar objetos 
arroz.vender(10)   # cuántas unidades
arroz.aplicar_descuento(20)  # porcentaje
televisor.vender(3)  # cuántas unidades
televisor.aplicar_descuento(15)  # porcentaje