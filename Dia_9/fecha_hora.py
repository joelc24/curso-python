from datetime import datetime, date


mi_fecha = datetime(2023, 5, 15, 22, 10, 15, 2500)
mi_fecha = mi_fecha.replace(month= 11)
print(mi_fecha)
nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)
vida = defuncion - nacimiento
minutos = datetime.today().minute
print(minutos)
print(vida)