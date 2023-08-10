class Coche:
    
    def __init__(self, color, modelo, marca):
        self.color = color
        self.modelo = modelo
        self.marca = marca
    


c = Coche("Rojo", "Coupe", "Chevrolet")
print(vars(c))

