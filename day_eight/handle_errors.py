
"""
    Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.

"""

"""
Ejemplo de resolución:
def nombre_funcion(argumento):
try:
{Lo que haría la función habitualmente}
except:
{Excepción}
else:
... etc.
"""

def suma(num1,num2):
    print(num1+num2)




"""

    Implementa para la siguiente función cociente(), un manejador de errores:

    Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"

    Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"

    En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) entre los dos números entregados como argumento.


"""



"""
Ejemplo de resolución:
def nombre_funcion(argumento):
try:
{Lo que haría la función habitualmente}
except:
{Excepción}
else:
... etc.
"""
def cociente(num1,num2):    
    print(num1/num2)
#MENSAJE EN PANTALLA











"""
    Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():

    En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"

    En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"

    Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"

    En todos los casos, al finalizar, imprimir: "Finalizando ejecución"

"""

"""
Ejemplo de resolución:
def nombre_funcion(argumento):
try:
{Lo que haría la función habitualmente}
except:
{Excepción}
else:
... etc.
"""

def abrir_archivo(nombre_archivo):
    archivo = open(nombre_archivo)
#MENSAJES EN PANTALLA: