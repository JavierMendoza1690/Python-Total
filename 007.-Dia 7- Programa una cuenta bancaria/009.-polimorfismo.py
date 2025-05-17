class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice muuu')


class Oveja:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice beeee')


#---Funcion indepeniente---

def animal_habla(animal):
    animal.hablar()


def main():
    vaca_1  = Vaca('Aurora')
    oveja_1 = Oveja('Nube')

    #polimorfismo basico
    '''dos objetos de clases distintas pueden llamar a un metodo con el mismo nombre'''
    vaca_1.hablar()
    oveja_1.hablar()

    #polimorfismo con interacion
    animales = [vaca_1,oveja_1]
    print() #salto de linea
    for animal in animales:
        animal.hablar()


    #polimorfismo con funciones
    print() #Salto de linea
    animal_habla(vaca_1)
    animal_habla(oveja_1)



if __name__ == '__main__':
    main()