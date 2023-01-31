def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


def chequear_3_cifras2(lista):
    return [n for n in lista if n in range(100, 1000)]


resultado = chequear_3_cifras([555, 99, 600])
resultado2 = chequear_3_cifras2([555, 99, 600])
print(resultado)
print(resultado2)
