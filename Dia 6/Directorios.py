import os
from pathlib import Path
# Obtener ruta del directorio actual
'''ruta = os.getcwd()'''
# Acceder a directorios distintos
'''other_route = os.chdir("C:\\Users\\ingri\\OneDrive\\Escritorio\\prueba_python")'''
# Crar carpeta en el directorio establecido
'''other_route = os.makedirs("C:\\Users\\ingri\\OneDrive\\Escritorio\\prueba_python\\otra")'''
ruta = 'C:\\Users\\WebMaster\\Desktop\\proyectos\\python\\curso-python\\Dia 6\\prueba.txt'
# Para obtener el nombre de base de nuestro elemento
'''elemento = os.path.basename(ruta)'''
# Para obtener ruta del directorio
'''elemento = os.path.dirname(ruta)'''
# Para obtener una tupla con el nombre del directorio y el nombre base
'''elemento = os.path.split(ruta)'''
# Eliminar directorio
'''os.rmdir("C:\\Users\\ingri\\OneDrive\\Escritorio\\prueba_python\\otra")'''

carpeta = Path("C:/Users/WebMaster/Desktop/Prueba")
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())