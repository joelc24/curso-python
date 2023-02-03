from collections import namedtuple, defaultdict

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 176, 79)
print(ariel)

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print()

