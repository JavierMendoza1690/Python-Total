from os import system

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre     = nombre
        self.apellido   = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        #invocando constructor del padre
        super().__init__(nombre,apellido)
        #creando atributos de instancia
        self.numero_cuenta  = numero_cuenta
        self.balance        =balance

    #Metoodos especiales

    def __str__(self):
        texto = (f'Nombre: {self.nombre}\n'
        f'Apellido: {self.apellido}\n'
        f'Numero de cuenta: {self.numero_cuenta}\n'
        f'Balance: {self.balance}')

        return texto

    #Metodos de instancia
    def depositar(self, cantidad_deposito):
        self.balance+=cantidad_deposito

    def retirar(self,cantidad_retiro):
        if (self.balance - cantidad_retiro) < 0:
            print('Fondos insuficientes')
            return

        print('Retiro realizado con exito')
        self.balance -= cantidad_retiro

#Funciones normales
def crear_cliente(nombre, apellido, numero_cuenta, balance):
    mi_cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    input('\nCuenta creada con exito')
    return  mi_cliente

def inicio():
    print('Por favor ingrese los datos de la cuenta a crear')

    nombre          = input('Ingrese su nombre: ')
    apellido        = input('Ingrese su apellido: ')
    numero_cuenta   = input('Ingrese el numero de cuenta que desea tener: ')
    balance         = int(input('Ingrese la cantidad de su primer deposito: '))

    cliente = crear_cliente(nombre,apellido,numero_cuenta,balance)

    system('cls')
    opcion = 1
    while(opcion != 3):
        print('\t\t\tMENU\t\t\t')
        print('¿Que desea hacer?')
        print('1.-Depositar')
        print('2.-Retirar')
        print("3.-Salir")
        opcion = int(input(''))
        match(opcion):
            case 1:
                system('cls')
                print('Ha elegido opcion 1\n')
                deposito = int(input('Ingrese cantidad a depositar: '))
                cliente.balance += deposito
                input(f'\nDeposito realizado exitosamente\nsu balance actual es {cliente.balance}\nPresione enter para continuar')
                system('cls')
            case 2:
                system('cls')
                print('Ha elegido opcion 2\n')
                retiro = int(input('Ingrese cantidad a retirar: '))
                if(cliente.balance - retiro < 0):
                    input('No tiene fondos suficientes\nPresione enter para continuar')
                    continue
                cliente.balance -= retiro

                input(
                    f'\nRetiro realizado exitosamente\nsu balance actual es {cliente.balance}\nPresione enter para continuar')
                system('cls')
            case 3:
                input('Gracias por su visita\nPresione enter para continuar')
            case _:
                print('Opcion invalida')

        system('cls')
def main():

  inicio()



if __name__ == '__main__':
    main()