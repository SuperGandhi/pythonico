
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
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_datos(self):
        print("Datos del Cliente:")
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Número de Cuenta: ", self.numero_cuenta)
        print("Balance: ", self.balance)

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Se depositó", cantidad, "a su cuenta. Balance actual:", self.balance)

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print("Se retiró", cantidad, "de su cuenta. Balance actual:", self.balance)
        else:
            print("Saldo insuficiente.")


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente


def inicio():
    cliente = crear_cliente()
    while True:
        print("\n1. Imprimir datos del cliente")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            cliente.imprimir_datos()
        elif opcion == 2:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == 3:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Intente nuevamente.")


inicio()
