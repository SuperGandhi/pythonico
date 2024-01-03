def age_high():
    user_entry = int(input("Ingrese su edad: "))

    if user_entry >= 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

result = age_high()
print(result)