
"""
    Cuenta bancaria
        crear class Persona
            atributos: nombre y apellido
        crear clase Cliente(Persona)
            atributos cliente: numero_cuenta y balance
            métodos :
                    imprimir los datos del cliente
                    depositar cuanto dinero quiere agregar a su cuenta
                    retirar cuanto dinero quiere sacar de su cuenta
        código para que el usuario elija si quiere Depositar,Retirar o Salir
            funciones:
                    crear_cliente()
                    inicio()
    
"""

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):
    
    def __init__(self,nombre,apellido,numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
        
    def mostrar_datos_cliente(self):
        
        print("Datos de cliente: ")
        print(f"Nombre: {self.nombre}")  
        print(f"Apellido: {self.apellido}")  
        print(f"Numero de cta: {self.numero_cuenta}")
        print(f"Balance: {self.numero_cuenta}")  
          
        
        
    def depositar(self):
        pass
    
    def retirar(self):
        pass
    