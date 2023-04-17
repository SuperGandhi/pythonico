"""
Crea una función (todos_positivos) que devuelva True si todos los valores de una lista (lista_numeros) son positivos, y False si al menos uno de los valores es negativo.

"""
def all_positives(list_numbers):
    for number in list_numbers:
        if number < 0:
            return False
    return True


result = all_positives([1,2,3,4])
print(result)


"""
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

"""






"""
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha suma.

"""