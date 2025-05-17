#--------CLASE ANIMAL------------
class Animal:

    def __init__(self, edad, color):
        self.edad   = edad
        self.color  = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

#--------CLASE PAJARO-------------
class Pajaro(Animal):

    #constructor hijo
    def __init__(self, edad, color, altura_vuelo):
        '''Forma no recomendada'''
        #self.edad   = edad
        #self.color  = color
        #self.altura_vuelo = altura_vuelo
        '''Forma recomendadda (SUPER)'''
        super().__init__(edad,color)  #invoca al constructor del padre
        self.altura_vuelo = altura_vuelo

    #sobreescribiendo el metodo hablar
    def hablar(self):
        print('Pio')
    def volar(self, metros):
        print(f'El pajaro vuela {metros}mts')

#---------MAIN--------
def main():
    #creando instancia de Pajaro (llamando al constructor hijo)
    piolin = Pajaro(2,'Amarillo',10)

    #creando instancia de la clase animal (constructor propio)-->Padre
    mi_animal = Animal(2,'rojo')

    #metodos heredados
    piolin.nacer()

    #metodos heredados - modificados
    piolin.hablar()

    #metodos nuevos - propios
    piolin.volar(5)

if __name__ == '__main__':
    main()
