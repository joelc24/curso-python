letters = ['a', 'b', 'c', 'd']
names = ['pablo','laura','fede','luis','julia']
numbers = [1,2,3,4,5]
mi_valor = 0
dic = {"clave1":"a","clave2":"b","clave3":"c"}

for letter in letters:
    numero_letra = letters.index(letter) + 1
    print(f"Letra: {numero_letra}: {letter}")

for name in names:
    if name.startswith('l'):
        print(name)
    else:
        print("Nombre que no comienza con l")


for number in numbers:
    mi_valor += number
print(mi_valor)

for letra in "python":
    print(letra)

for numero in (1,2,3,4):
    print(numero)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

for item in dic.items():
    print(item)