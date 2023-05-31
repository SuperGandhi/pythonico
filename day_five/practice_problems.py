



"""
    Crea una función llamada devolver_distintos() que reciba 3
    integers como parámetros.
    Si la suma de los 3 numeros es mayor a 15, va a devolver el
    número mayor.
    Si la suma de los 3 numeros es menor a 10, va a devolver el
    número menor.
    Si la suma de los 3 números es un valor entre 10 y 15
    (incluidos) va a devolver el número de valor intermedio.
    
"""
def devolver_distintos(*args):
    if len(args) != 3:
        return "La función debe recibir exactamente 3 enteros como argumentos."

    suma = sum(args)

    if suma > 15:
        return max(args)
    elif suma < 10:
        return min(args)
    else:
        return sorted(args)[1]

# Solicitar al usuario que ingrese los valores
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

resultado = devolver_distintos(num1, num2, num3)
print("El resultado es:", resultado)




"""
    Escribe una función (puedes ponerle cualquier nombre que
    quieras) que reciba cualquier palabra como parámetro, y que
    devuelva todas sus letras únicas (sin repetir) pero en orden
    alfabético.
    Por ejemplo si al invocar esta función pasamos la palabra
    "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
        
"""
















"""
    Escribe una función que requiera una cantidad indefinida de
    argumentos. Lo que hará esta función es devolver True si en
    algún momento se ha ingresado al numero cero repetido dos
    veces consecutivas.
    Por ejemplo:
    (5,6,1,0,0,9,3,5) >>> True
    (6,0,5,1,0,3,0,1) >>> False

"""















"""
    Escribe una función llamada contar_primos() que requiera un
    solo argumento numérico.
    Esta función va a mostrar en pantalla cuántos números
    primos hay en el rango que va desde cero hasta ese número
    incluido, y va a devolver la cantidad de números primos que
    encontró.
    Aclaración, por convención el 0 y el 1 no se consideran primos.

"""

