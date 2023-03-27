
greeting_user = input("What is your name?: ")
print(f"Hi {greeting_user} think one number between 1 and 100 you only have eight tries to guess it!, Let's go!")

entry_user_number = int(input("Please entry your number: "))

if entry_user_number < 1 and entry_user_number > 100:
   print("Este número no está permitido")
elif entry_user_number < 1 and entry_user_number < 100:
   print("El número ingresado es menor")
elif entry_user_number > 100:
   print("El número ingresado es mayor")
elif entry_user_number == entry_user_number.random():
   print("Ganaste!")
else:
   print("Sigue intentando!")