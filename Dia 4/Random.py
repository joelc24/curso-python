from random import *
colores = ['azul','rojo','verde','amarillo']
numeros = list(range(5, 51, 5))
aleatorio = randint(1,50)
aleatorio2 = round(uniform(1,5),1)
aleatorio3 = random()
aleatorio4 = choice(colores)
print(aleatorio)
print(aleatorio2)
print(aleatorio3)
print(aleatorio4)

shuffle(numeros)
print(numeros)