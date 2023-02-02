class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice muuu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice bee")


vaca1 = Vaca("Lola")
oveja1 = Oveja("Nube")

'''animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()'''

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)