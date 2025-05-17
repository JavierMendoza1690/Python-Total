from collections import defaultdict

#mi_dic = {'uno':'verde', 'dos':'azul', 'tres': 'rojo'}
#print(mi_dic['cuatro'])

mi_dic = defaultdict(lambda: 'nada')        #cuando hay una clave que no exista asigna nada y la crea

#asignando un nuevo valor al diccionario
mi_dic['uno'] = 'verde'

print(mi_dic['dos'])        #nada
print(mi_dic)               #defaultdict(<function <lambda> at 0x000001D2CE248720>, {'uno': 'verde', 'dos': 'nada'})