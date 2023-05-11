from random import randint,choice

"""
Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados (la función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:dado_a,dado_b

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


"""
def lanzar_dados():
    dado_a = randint(1,6)
    dado_b = randint(1,6)
    return dado_a,dado_b

resultado1, resultado2 = lanzar_dados()
print("El primer dado arrojó un resultado de", resultado1)
print("El segundo dado arrojó un resultado de", resultado2)


def evaluar_jugada(resultado1, resultado2):
    total_result = resultado1 + resultado2
    if total_result <= 6:
        return f"La suma de tus dados es {total_result} . Lamentablemente"
    elif total_result < 10:
        return f"La suma de tus dados es {total_result} . Tienes buenas chances"
    else:
        return f"La suma de tus dados es {total_result} . Parece una jugada ganadora"

resultado1, resultado2 = lanzar_dados()
message= evaluar_jugada(resultado1, resultado2)
print(message)


"""

Práctica sobre Interacción entre Funciones 2
Crea una función llamada reducir_lista() que tome una lista (lista_numeros) como argumento, y devuelva la misma lista, pero eliminando duplicados (dejando un solo número si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Emplea la lista devuelta por la primera función y calcula el promedio de los valores de sus elementos, creando una nueva función llamada promedio().

"""
def reducir_lista(lista_numeros):
    # Eliminar duplicados y encontrar el valor máximo
    numeros_unicos = list(set(lista_numeros))
    max_valor = max(numeros_unicos)
    
    # Eliminar el valor máximo de la lista
    numeros_unicos.remove(max_valor)
    
    return numeros_unicos


def promedio(lista_numeros):
    # Calcular la suma de los elementos
    suma = sum(lista_numeros)
    
    # Calcular el promedio
    promedio = suma / len(lista_numeros)
    
    return promedio


# Ejemplo de uso
lista = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista)
promedio_valores = promedio(lista_reducida)

print("Lista reducida:", lista_reducida)
print("Promedio de valores:", promedio_valores)














"""
Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

"""