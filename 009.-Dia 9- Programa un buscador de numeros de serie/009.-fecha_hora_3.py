#CALCULAR TIEMPO ENTRE DOS FECHAS

from datetime import date


#CALCULO VIDA UNA PERSONA

nacimiento = date(1995,3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento

print(vida)         #36631 days, 0:00:00
print(vida.days)    #36631

