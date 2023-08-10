class Coche:
    
    def __init__(self, color, modelo, marca):
        self.color = color
        self.modelo = modelo
        self.marca = marca
    


c = Coche("Rojo", "Coupe", "Chevrolet")
setattr(c, "num_ruedas", 5)

print(getattr(c, "marca"))

delattr(c, "marca")

print(hasattr(c, "marca"))

print(vars(c))

