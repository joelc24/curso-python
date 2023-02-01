from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
# Asi cambiamos el archivo de destino
guia2 = guia.with_name("La_Pedrera.txt")
print(base)
print(guia)
print(guia2)
print(guia.parent.parent.parent)