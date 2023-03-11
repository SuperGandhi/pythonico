"""
Práctica Control de Flujo 1 Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado): Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso: "num1 es mayor que num2" "num2 es mayor que num1" "num1 y num2 son iguales" Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2. num1 = input("Ingresa un número:") num2 = input("Ingresa otro número:") f"{num1} es mayor que {num2}" "num1 es mayor que num2" "num1 y num2 son iguales"

"""
num1 = int(input("Entry the firts number: "))
num2 = int(input("Entry the second number: "))


if num1 > num2:
    print(f"{num1} is mayor of {num2}")
elif num2 > num1:
   print(f"{num2} is mayor of {num1}")
else:
   print(f"{num1} and {num2} are equivalent")

    