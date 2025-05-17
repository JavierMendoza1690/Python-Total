'''Escribe una función que requiera una cantidad indefinida deargumentos. Lo que hará esta función es devolver
True
si enalgún momento se ha ingresado al numero
cero
repetido dosveces consecutivas
.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>>
True
(6,0,5,1,0,3,0,1) >>>
False'''

def dos_ceros_consecutivos(*args):

    for i in range(0,len(args)-1):
        if(args[i] == args[i+1] and args[i]==0):
            return True
        else:
            pass
    return False


print(dos_ceros_consecutivos(3,3,2,0,0,9,2,))
