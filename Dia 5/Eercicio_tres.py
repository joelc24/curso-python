def ceros_vecinos(*args):
    contador = 0

    for n in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False


print(ceros_vecinos(5, 6, 8, 5, 0, 4, 9, 7, 5, 2, 7, 0))