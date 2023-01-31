def devolver_distintos(n1, n2, n3):
    lista_numeros = [n1, n2, n3]
    suma = sum(lista_numeros)
    if suma in range(10, 15):
        lista_numeros.sort()
        return lista_numeros[1]
    elif suma < 10:
        return min(lista_numeros)
    else:
        return max(lista_numeros)


print(devolver_distintos(1, 2, 5))