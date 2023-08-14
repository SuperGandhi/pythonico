class Fabrica:
    
    def __init__(self,llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    

class Moto(Fabrica):
    
    def data(self):
        print("La cantidad de llantas es de: ", self.llantas)
        print("El color de la moto es: ", self.color)
        print("El precio de la moto es: ", self.precio)

class Carro(Fabrica):
    
        def data(self):
            print("La cantidad de llantas es de: ", self.llantas)
            print("La color del carro es: ", self.color)
            print("El precio del carro es: ", self.precio)
        

moto = Moto(2,"verde",5000)
moto.data()
carro =  Carro(4,"negro", 2000)
carro.data()











    


        
        