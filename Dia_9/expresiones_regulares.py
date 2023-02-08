import re

texto = "Llama al 654-525-6588 ya mismo"

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
busqueda = re.search(patron, texto)

print(busqueda.group(3))

texto = "No atendemos los lunes por la tarde"
buscar = re.search(r'lunes|martes', texto)
print(buscar.group())