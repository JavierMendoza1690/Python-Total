class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color      = color
        self.especie    = especie
    #Metodos Piar sin atributos
    def piar(self):
        print('Pio')
        #pasando variables forma antigua
        print('Mi color es {}'.format(self.color))
        #pasando variables forma moderna
        print(f'Mi especie es {self.especie}')

    # Metodos volar con atributos
    def volar(self,metros):
        print(f'Voló {metros}mts')

piolin = Pajaro('Amarillo','Canario')

#llamando metodo piar
piolin.piar()

#llamando al metodo volar
piolin.volar(40)