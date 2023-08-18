# generadores
# decoradores

# perfumeria = ["P-100","P-102","P-103","P-104","P-105","P-106" ]
# farmacia = ["F-100","F-102","F-103","F-104","F-105","F-106" ]
# cosmetica = ["C-100","C-102","C-103","C-104","C-105","C-106" ]

def numeros_perfumeria():
    for n in range(1,100):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1,100):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1,100):
        yield f"C - {n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


# def decorator(rubro):
    
# print(numeros_cosmetica \n)
