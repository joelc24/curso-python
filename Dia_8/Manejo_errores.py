def suma():
    n1 = input("Numero 1: ")
    n2 = input("Numero 2: ")
    print(n1 + n2)
    print("Gracias por sumar")


try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")