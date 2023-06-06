"""
    Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.
    Completa el código suministrado a continuación para lograrlo.

"""
class Padre:
    
    def trabajar(self):
        print("Trabajando en el hospital")


    def reir(self):
        print("Hahahaha")


class Madre():
    def trabajar(self):
        print("Trabajando con la Fiscalia")


class Hija(Madre, Padre):
    pass



"""

    "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)

    Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:

    - poner_huevos()

    - tiene_pico = True

    - vertebrado = True

    - venenoso = True

    - nadar()

    - caminar()

    - amamantar()


"""

class Vertebrado:
    
    vertebrado = True

class Ave(Vertebrado):
    
    tiene_pico = True
    
    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    
    venenoso = True
    
class Pez(Vertebrado):

    def nadar(self):
        print("Nadando")
    
    def poner_huevos(self):
        print("Poniendo huevos")


class Ornitorrinco(Ave,Reptil,Pez):
    
    def __init__(self):
        super().__init__()

    def caminar(self):
        print("Caminando ando")








"""
    Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"



    [1]: asegúrate de utilizar return seguido de una cadena de texto


"""



class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    
    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo():
        pass
        "Juego videojuegos en mi tiempo libre"