from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/WebMaster/Desktop/proyectos/python/curso-python/Dia 6/prueba1.txt")
ruta_windows = PureWindowsPath(carpeta)
# Para leer el archivo
'''print(carpeta.read_text())'''
# Obtener nombre
'''print(carpeta.name)'''
# Sirve para ver la terminacion del archivo y saber que tipo de archivo es
'''print(carpeta.suffix)'''
# Obtener el nombre sin la terminacion
'''print(carpeta.stem)'''
# Para validar si el archivo existe
'''if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")'''

print(ruta_windows)