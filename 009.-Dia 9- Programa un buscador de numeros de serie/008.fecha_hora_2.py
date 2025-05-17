#COMBINAR FECHA Y HORA

from datetime import datetime

#estableciendo fecha
mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 1500)

mi_fecha = mi_fecha.replace(month = 11)

print(mi_fecha)     #2025-05-15 22:10:15.001500

