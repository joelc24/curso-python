# Bad Form
lista = ['a','b','c']
indice = 0
mis_tuples = list(enumerate(lista))

for item in lista:
    print(indice,item)
    indice += 1

# Good Form
for i, letra in enumerate(lista):
    print(i,letra)

for i, letra in enumerate(range(50,56)):
    print(i,letra)
print(mis_tuples)
