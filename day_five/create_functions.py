"""
Práctica Crear Funciones 1 Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

"""
def greeting():
    print("Hi World")

greeting()



"""
Práctica Crear Funciones 2 Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!" Para probar su funcionamiento, crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

"""

def welcome_greeting(name):
    print(f"¡Welcome {name}!")

welcome_greeting("Julian")


"""
Práctica Crear Funciones 3 Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor). El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera para probar la función creada.

"""

def number_quadrade(n):
   n = n ** 2
   print(n)

number_quadrade(2)