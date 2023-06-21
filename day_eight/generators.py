
"""
    Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

"""

def generator_infinito():
    num = 1
    while True:
        yield num
        num += 1
        
generator = generator_infinito()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


"""
    Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

"""













"""
    
     Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:

    "Te quedan 3 vidas"

    "Te quedan 2 vidas"

    "Te queda 1 vida"

    "Game Over"

    Almacena el generador en la variable perder_vida
    

"""