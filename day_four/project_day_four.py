from random import randint


trying_find_number = 0
greeting_user_trying = 0
secret_number = randint(1,100)
user_name = input("Tell me your name: ")

print(f"Hi {user_name} you have eight chances to guess the secret number, don't forget think a number between 1 and 100")

while trying_find_number < 8:
   greeting_user_trying = int(input("What is the number?: "))
   trying_find_number += 1

   if greeting_user_trying < secret_number:
      print("The number is a litle bit more large")
   elif greeting_user_trying > secret_number:
      print("The number is a litle bit more small")
   elif greeting_user_trying != secret_number:
      print(f"I'm sorry, you don't have any more chances")
   else:
      print(f"Congratulations! {user_name} Your rock! in {trying_find_number} tries")


