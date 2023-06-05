"""
    Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

    Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.

"""

class Casa:
    
    def __init__(self,color,cantidad_pisos ):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanca", 4)
print(f"Mi casa es {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos")


"""
    Crea una clase llamada Cubo, y asígnale el atributo de clase:

    caras = 6

    y el atributo de instancia:

    color

    Crea una instancia cubo_rojo, de dicho color.

"""

class Cubo:
    
    def __init__(self,caras,color):
        self.caras = caras
        self.color = color
        
cube = Cubo(10,"negro")

print(f"Mi cubo tiene {cube.caras} caras y es de color {cube.color}")


"""

    Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

    real = False

    Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

    especie = "Humano"

    magico = True

    edad = 17

"""

class Personaje:
    real = False

harry_potter = Personaje()
harry_potter.especie = "Humano"
harry_potter.magico = True
harry_potter.edad = 17
        

