class Animal:

    def __init__(self, edad, color):
        self.edad   = edad
        self.color  = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass


def main():
    #Inspeccionando el padre de Pajaro
    print(Pajaro.__bases__) #(<class '__main__.Animal'>,)

    #Inspeccionando los hijos de Animal
    print(Animal.__subclasses__()) #[<class '__main__.Pajaro'>]

    #Creando una instancia de Pajaro con el constructor del padre (Animal)
    piolin = Pajaro( 10, 'Amarillo')
    #Invocando metodo nacer del padre
    piolin.nacer()

    #imprimiendo el atributo color de piolin (lo tiene piolin pero lo hereda del padre)
    print(piolin.color)

if __name__ == '__main__':
    main()