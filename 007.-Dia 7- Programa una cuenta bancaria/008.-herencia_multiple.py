class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja Ja Ja')
    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


def main():
    mi_nieto = Nieto()

    #llamando metodo del padre
    mi_nieto.hablar() #Hereda el del primero en la herencia

    #llamando metodo de la madre
    mi_nieto.reir()

    #invocando __mro__(method order resolution)
    '''Da el orden donde en el que buscará metodos dentro de las clases '''
    print(Nieto.__mro__) #(<class '__main__.Nieto'>, <class '__main__.Hijo'>, <class '__main__.Padre'>, <class '__main__.Madre'>, <class 'object'>)

if __name__ == '__main__':
    main()