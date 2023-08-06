class TeslaVehicles:
    
    def __init__(self, *colors, **kinds):
        self.kinds = kinds
        self.colors = colors
        


modelo_s = TeslaVehicles("black" , sportive = "luxury")
print(modelo_s.kinds)
print(modelo_s.colors)
