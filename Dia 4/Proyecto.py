from random import randint
i = 8
number_random = randint(1,100)
name_user = input("¿Cual es tu nombre? \n")
print(f"Hola {name_user} he pensado un numero entre el 1 y el 100.. \nTienes 8 intentos para adivinar cual es")
print('-'*100)

while i > 0:
    number = int(input("¿Cual es el numero? \n"))
    if number < 0:
        print("Has digitado un numero no permitido \n por favor digite solo numeros positivos")
    elif number < number_random:
        print("El numero ingresado es menor al numero que pense")
    elif number > number_random:
        print("El numero ingresado es mayor al numero que pense")
    else:
        print(f"Has acertado!! \nTe tomo {8 - i} intentos")
        break
    i -= 1
else:
    print("Game Over! 😢😢")

