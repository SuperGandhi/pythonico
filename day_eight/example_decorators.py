def decorar_saludo(funcion):
    
    
    def otra_funcion(palabra):
        print("Hi")
        funcion(palabra)
        print("Bye")
    return otra_funcion

@decorar_saludo
def mayusculas(text):
    pass