text_user = input('Entry your text: ')
letters_user = []
text_user = text_user.lower()

letters_user.append(input('Enter the firts letter: ').lower()) 
letters_user.append(input('Enter the second letter: ').lower()) 
letters_user.append(input('Enter the third letter: ').lower())

print("\n")
print("Amount letters: ")


amount_letters1 = text_user.count(letters_user[0])
amount_letters2 = text_user.count(letters_user[1])
amount_letters3 = text_user.count(letters_user[2])

print(f"We find the '{letters_user[0]}' repeat{amount_letters1} times")

print(f"We find the '{letters_user[1]}' repeat{amount_letters1} times")

print(f"We find the '{letters_user[2]}' repeat{amount_letters1} times")