class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color      = color
        self.especie    = especie
    #Metodos de instancia
    '''
    Acceden y modifican atributos del objeto
    Acceden a otros metodos si lo desean
    Modifican el estado de la clase(atributos de clase) si se desea
    '''
    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')
        #pueden llamar a otros metodos
        self.piar()


    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    #Metodos de clase
    '''
    Similares a una metodo estatico en Java
    No necesitan una clase para poder ejecutarse
    No puede acceder a los atributos de los objetos
    Puede acceder a los atributos de clase (Globales)
    '''
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        #print(f'Es de color {self.color}') #Error
        cls.alas = False
        print(Pajaro.alas)  # modifica las a alas de toda la clase

    #Metodo estatico
    '''
    Similar a una funcion pero con la salvedad que es perteneciente a una clase
    No se puede relacionar con instancias
    No se puede relacionar con atributos de la clase
    '''
    @staticmethod
    def mirar():
        print('Puedo hacer lo de una funcion normal solamente')


piolin = Pajaro('amarillo','canario')
#pintando a piolin de negro
piolin.pintar_negro()
#invocando metodo volar de la clase Pajaro
piolin.volar(50)
#modificando los atributos de clase
piolin.alas = False

#imprimiendo las alas de piolin
print(piolin.alas)

#invocando el metodo de claes (estatico)
Pajaro.poner_huevos(3)
print(Pajaro.alas)   #modifica la clase entera

pajaro2 = Pajaro('blanco', 'paloma')
print(pajaro2.alas)  # de ebtrada sin alas ya que se accedio a a las alas con Pajaro.alas y cambio para todos

#invocando metodo esttico
Pajaro.mirar()
