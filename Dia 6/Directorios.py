import os

ruta = os.getcwd()
'''other_route = os.chdir("C:\\Users\\ingri\\OneDrive\\Escritorio\\prueba_python")'''
other_route = os.makedirs("C:\\Users\\ingri\\OneDrive\\Escritorio\\prueba_python\\otra")
archivo = open("prueba.txt")
print(archivo.read())