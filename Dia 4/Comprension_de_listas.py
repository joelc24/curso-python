palabra = 'python'
pies = [10,20,30,40,50]
metros = [pie * 3.281 for pie in pies]

lista = [letra for letra in 'palabra']
lista2 = [n for n in range(0,21,2)]
lista3 = [n / 2 for n in range(0,21,2)]
lista4 = [n for n in range(0,21,2) if n * 2 > 10]
lista5 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]


print(lista)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(pies)
print(metros)