"""
   Práctica Loop While 1 Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez. numero = 10

"""

numero = 11

while numero > 0:
   numero -= 1
   print(numero)

"""
   Práctica Loop While 2 Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales: - Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!) - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente). numero = 50

"""

numero = 51

while numero > 0:
   numero -= 1
   if numero % 5 == 0:
      print("¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto¡")



"""
   Práctica Loop While 3 Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo: lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3] No debes cambiar el orden de la lista. 

"""

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for lista in lista_numeros:
   if lista < 0:
      break
   print(lista)



