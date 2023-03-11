"""
Práctica Loop For 1 Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre. Por ejemplo: "Hola María" alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"] 

"""

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"] 

for greeting in alumnos_clase:
  print(f"Hi {greeting}")


"""
Práctica Loop For 2 Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros: lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] suma_numeros =

"""

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_numeros = 0

for numeros in lista_numeros:
  sum_numeros += numeros

print(f"La suma de los numeros es: {sum_numeros}")