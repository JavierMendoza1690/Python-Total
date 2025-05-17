


#CREANDO GENERADORES

#generador perfumeria
def turno_perfumeria():
    contador_perfumeria =0
    while True:
        contador_perfumeria+=1
        yield f'P-{contador_perfumeria}'

def turno_farmacia():
    contador_farmacia=0
    while True:
        contador_farmacia+=1
        yield f'F-{contador_farmacia}'

def turno_cosmeticos():
    contador_cosmeticos =0
    while True:
        contador_cosmeticos+=1
        yield f'C-{contador_cosmeticos}'


p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmeticos()



#CREANDO DECORADOR
def decorar_turno(rubro):

    print('Su numero es: ')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    elif rubro =='C':
        print(next(c))

    print('Aguarde y sera atendido')


