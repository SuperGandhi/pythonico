"""
Práctica Control de Flujo 1 Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado): Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso: "num1 es mayor que num2" "num2 es mayor que num1" "num1 y num2 son iguales" Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.

"""
num1 = int(input("Entry the firts number: "))
num2 = int(input("Entry the second number: "))


if num1 > num2:
    print(f"{num1} is mayor of {num2}")
elif num2 > num1:
   print(f"{num2} is mayor of {num1}")
else:
   print(f"{num1} and {num2} are equivalent")


"""
Práctica Control de Flujo 2 Las leyes de un país establecen que un adulto puede conducir si es mayor de edad (tiene 18 años o más), y cuenta con una licencia para conducir. Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla: "Puedes conducir" "No puedes conducir aún. Debes tener 18 años y contar con una licencia" "No puedes conducir. Necesitas contar con una licencia".

"""
user_entry = int(input("How old are you?: "))
#                             age = 16
license_drive = input("You have a license drive, please responds with yes or no: ")

if user_entry >= 18 and license_drive == "yes":
   print(f"Yes, you can drive because you have {user_entry} years old  and also have license drive")
elif user_entry < 18:
   print(f"No, you can't drive because yo have {user_entry} years old")
elif user_entry >= 18 or license_drive == "no":
   print(f"You have the correct age to drive, but you don't have the license to drive")
else:
   print("Please complete the questions!")


"""

Práctica Control de Flujo 3 Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés. Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla: "Cumples con los requisitos para postularte" "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés" "Para postularte, necesitas tener conocimientos de inglés" "Para postularte, necesitas saber programar en Python" Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python. habla_ingles = True sabe_python = False "Cumples con los requisitos para postularte" "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés" "Para postularte, necesitas tener conocimientos de inglés" "Para postularte, necesitas saber programar en Python"

"""

speak_english = True
meet_python = False

if speak_english and not(meet_python):
   print("You rock!")
elif speak_english or meet_python:
   print("You need know python")
elif not(speak_english) or meet_python:
   print("You need speak English babe")
else:
   print("You need have a strong background in python and proficient english babe")












