
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