## proyecto que consiste en crear un còdigo
# que le permita a una persona realizar operaciones en su cuenta bancaria

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Hola {self.nombre} {self.apellido}\nsu numero de cuenta {self.numero_cuenta} tiene un saldo de: S/.{self.balance}'

    def depositar(self,d):
        self.balance = self.balance + d
        print(f"Su deposito de S/.{d} se ejecutò correctamente")

    def retirar(self,r):
        if self.balance >= r:
            self.balance = self.balance - r
            print(f"Su retiro de S/.{r} se ejecutò correctamente")

        else:
            print("Saldo insuficiente")


def crear_cliente():
    nombrec = input('Estimado cliente ingrese su nombre ')
    apellidoc = input('Estimado cliente ingrese su apellido ')
    numero_cuentac = input('Estimado cliente ingrese su numero de cuenta ')
    clientec = Cliente(nombrec,apellidoc,numero_cuentac)
    return clientec

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    c1 = ''
    while c1 != 'S':
        c1 = input("Estimado cliente elija la opciòn a realizar Depositar (D) Retirar (R) Salir(S)\n")
        if c1 == 'D':
            n = int(input('Ingrese el monto a depositar '))
            mi_cliente.depositar(n)
        elif c1 == 'R':
            n = int(input('Ingrese el monto a retirar '))
            mi_cliente.retirar(n)
        print(mi_cliente)
    print(f"Muchas gracias, esperamos verlo pronto")

inicio()