class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    @staticmethod
    def nacer():
        print("Este animal ha nacido")

    @staticmethod
    def hablar():
        print("Este animal emite un sonido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    @staticmethod
    def hablar():
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


piolin = Pajaro(3, 'amarillo', 60)
mi_animal = Animal(5, 'negro')

piolin.nacer()
piolin.hablar()
piolin.volar(100)
