class Padre:
    @staticmethod
    def hablar():
        print("Hola")


class Madre:
    @staticmethod
    def reir():
        print("JA JA JA")

    @staticmethod
    def hablar():
        print("Que tal")

class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()


