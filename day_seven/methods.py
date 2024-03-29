"""
    Crea una clase Perro. Dicho perro debe poder ladrar.

    Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

"""

class Perro:
    
    def __init__(self,raza,color,años):
        self.raza = raza
        self.color = color
        self.años = años

    def ladrar(self):
        print('Guau!')


bull_terrier = Perro("bullterrier", "blanco", 10)
bull_terrier.ladrar()

print(f"Mi perro es un {bull_terrier.raza} de color {bull_terrier.color} y tiene {bull_terrier.años}")



"""
    Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

    Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

"""

class Mago:
    
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()


"""
    Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

    "La alarma ha sido pospuesta {cantidad_minutos} minutos"

"""


class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
alarma = Alarma()
alarma.postergar(20)



