import numeros as n

def greeting():
    message = input("Hola a que sección desea dirigirse: ")
    
    if message == "perfumeria":
        return n.numeros_perfumeria
    elif message == "farmacia":
        return n.numeros_farmacia
    else:
        return n.numeros_cosmetica
    
    

result = greeting()
print(result)
