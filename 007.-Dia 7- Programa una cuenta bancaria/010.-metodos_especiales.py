class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        '''
        me ayuda a definir la forma de mostrar un string de mi clase
        cada vez que un metodo lo solicite
        '''

        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        '''
        definiendo como se va a comportar len
        '''
        return self.canciones

    def __del__(self):
        print('Se ha eliminado el cd')


def main():
    mi_cd = CD('Pink Floyd', 'The Wall', 24)
    #print(mi_cd)        #<__main__.CD object at 0x00000247AA75D280> antes de __str__
    print(mi_cd)         #Album: The Wall de Pink Floyd

    print(len(mi_cd))   #24 gracias a __len__ de lo contrario sería error

    #eliminar instancia que haya creado
    del mi_cd            # muestra el mensaje "Se ha eliminado el cd" gracias a __del__

    #print(mi_cd)        #error fue eliminada la instancia



if __name__ == '__main__':
    main()