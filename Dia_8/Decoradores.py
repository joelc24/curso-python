def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hello")
        funcion(palabra)
        print("Bye")
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayusculas)
mayusculas("Joel")
mayuscula_decorada("Joel")