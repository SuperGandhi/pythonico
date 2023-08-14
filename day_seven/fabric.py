class Fabrica:
    
    def __init__(self,llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    

class Moto(Fabrica):
    pass

class Carro(Fabrica):
    pass


        
        