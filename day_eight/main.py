import numeros as n

def greeting():
    message = input("Hola a que sección desea dirigirse: ")
    
    if message == "perfumeria":
        return n.perfumeria
    elif message == "farmacia":
        return n.farmacia
    else:
        return n.cosmetica
    
    

result = greeting()
print(result)

def generator():
    pass
