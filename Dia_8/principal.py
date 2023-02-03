import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")
    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubru = input("Elija su rubru: ").upper()
            ["P", "F", "C"].index(mi_rubru)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    numeros.decorador(mi_rubru)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == 'N':
                print("Gracias por su visita")
                break


inicio()

