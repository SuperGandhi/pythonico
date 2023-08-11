
"""
    La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.

    Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

    Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html


"""

 
# Definición de los objetos
palabra = "Hola"
lista = [1, 2, 3, 4, 5]
tupla = (6, 7, 8, 9, 10)

# Creación del iterador
objetos = [palabra, lista, tupla]

# Recorriendo los objetos y mostrando su longitud
for objeto in objetos:
    longitud = len(objeto)
    print("El objeto", objeto, "tiene una longitud de", longitud)




"""

    Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

    Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.


"""



class Arquero:
    
    def attack(self):
        return "Arquero : Damage 50"    

class Mago:
    
    def attack(self):
        return "Mago: Damage 30" 
    
class Samurai:
    
    def attack(self):
        return "Samarui: Damage 70" 



arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero,mago,samurai] 

for personaje in personajes:
    print(personaje.attack())
    


"""

    Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.

    Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.


"""

# class Personaje:
    
#     def fire_defense(self):
#         return "Fire defense"

#     def ice_defense(self):
#         return "Ice defense"
        
#     def wind_defense(self):
#         return "Wind defense"


# fire_offensive = Personaje()

# def personaje_defender(self):
#     print(fire_offensive.fire_defense())



class Guerrero:
    def defender(self):
        return "Guerrero defendiendo con su escudo."

class Mago:
    def defender(self):
        return "Mago invocando un escudo mágico."

class Arquero:
    def defender(self):
        return "Arquero esquivando y utilizando su agilidad para defenderse."

def personaje_defender(personaje):
    if hasattr(personaje, 'defender') and callable(getattr(personaje, 'defender')):
        return personaje.defender()
    else:
        return "El personaje no tiene un método de defensa válido."

# Creación de instancias de personajes
guerrero = Guerrero()
mago = Mago()
arquero = Arquero()

# Llamada a la función personaje_defender() con diferentes personajes
print(personaje_defender(guerrero))
print(personaje_defender(mago))
print(personaje_defender(arquero))


# other example

class Animals:
    
    def __init__(self, message):
        self.message = message
        
    def talk(self):
        print(self.message)
        
class Dog(Animals):
    
    # modificar métodos heredados de una clase padre
    def talk(self):
        print("I don't talk , but I do guau!")


class Fish(Animals):
    
    def talk(self):
        print("I dont talk")
        
        
dog = Dog("Guau!")
dog.talk()

        
        
        
        
        
        
        
        
        