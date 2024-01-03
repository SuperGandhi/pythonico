# función que indique cuantas vocales tiene una palaba o un string

word = 'hola como estas'
vocals = 0

for letter in word:
    vocals += 1 if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' else 0

print(vocals)