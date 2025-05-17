#CALCULO HORAS QUE UNA PERSONA ESTUVO DESPIERTA

from datetime import datetime

despierta   = datetime(2022,10,5,7,30)
duerme      = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta

print(vigilia)              #16:15:00
print(vigilia.seconds)      #58500