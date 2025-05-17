#Definiendo clase pajaro
class Pajaro:

    #atributos de clase
    alas = True  #todos los pajaros tendrán alas

    #Definiendo constructor pajaro (__init__) que es la representacion de que requiere la clase
    def __init__(self, mi_parametro, especie):
        '''
        self representa la instancia del objeto que va a ser creado
        self.atributo significa que se está creando un atributo llamado 'atributo'
        '''

        #inicializando los atributos por medio del constructor
        #creando un atributo que se llama 'atributo y se iguala al parametro del constructor
        self.atributo = mi_parametro

        #creando un atributo especie que es igual al valor del parametro especie
        self.especie = especie






#-------------------MAIN--------------------------

def main():
    #mi_pajaro = Pajaro() #Error falta argumento color


    mi_pajaro = Pajaro('negro','Tucan')

    #imprimiendo el el atributo llamado "atributo" de mi_pajaro
    print(mi_pajaro.atributo) #negro

    #imprimiendo la especie de mi pajaro
    print(mi_pajaro.especie) #Tucan

    #sobreescribiendo el atributo color
    mi_pajaro.color = 'blanco'

    #Imprimiendo un atributo de clase: iguales para todos los objetos (como atributos estaticos)
    print('Alas',Pajaro.alas)

if(__name__ =='__main__'):
    main()

