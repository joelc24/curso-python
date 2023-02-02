class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance


    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"


    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente


def inicio():
    cliente = crear_cliente()
    print(cliente)
    opcion = 0

    while opcion != "S":
        print("Elige: Depositar (D), Retirar (R), o Salir (S)")
        opcion = input()

        if opcion == "D":
            monto_deposito = int(input("Monto ha depositar: "))
            cliente.depositar(monto_deposito)
        elif opcion == "R":
            monto_retiro = int(input("Monto a retirar: "))
            cliente.retirar(monto_retiro)
        print(cliente)
    print("Gracias por operar en Banco Python")


inicio()