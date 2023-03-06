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

print(f"We find the '{letters_user[0]}' repeat {amount_letters1} times")

print(f"We find the '{letters_user[1]}' repeat {amount_letters1} times")

print(f"We find the '{letters_user[2]}' repeat {amount_letters1} times")

print("\n")
print("Amount of words: ")
words = text_user.split()
print(f"* We find {len(words)} words in your text")

print("\n")
print("Init letter and end letter: ")
letter_init = text_user[0]
letter_end = text_user[-1]
print(f"* The letter init is '{letter_init}' and the end is '{letter_end}'")


print("\n")
print("* The reverse text : ")
words.reverse()
text_reverse = ' '.join(words)
print(f"    *Your text reverse look as: {text_reverse}")

print("\n")
print("Find the word python in your text")
find_python = 'python' in text_user
dic = {True: "yes in the text", False: "don't in the text"}
print(f"* The word python {dic[find_python]}")