mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2
resultado = mi_lista[0:]

mi_lista3.append("g")
eliminado = mi_lista3.pop(-1)

lista_desordenada = ["g","o","b","m","c"]
lista_desordenada.sort()
lista_desordenada.reverse()
print(lista_desordenada)