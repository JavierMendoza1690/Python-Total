import datetime

#date.time usa un formato de 24 horas (horas,minutos,segundos,...)
mi_hora = datetime.time(17, 35,50,1500)

print(type(mi_hora))        #<class 'datetime.time'>
print(mi_hora)              #17:35:50.001500
print(mi_hora.hour)         #17
print(mi_hora.minute)       #35


#TRABAJANDO CON FECHAS
mi_dia = datetime.date(2025,10,17)

print(mi_dia)           #2025-10-17

print(mi_dia.year)      #2025

#mostrando informacion en formato distinto

print(mi_dia.ctime())   #Fri Oct 17 00:00:00 2025

#fecha del dia de hoy
print(mi_dia.today())   #2025-05-09