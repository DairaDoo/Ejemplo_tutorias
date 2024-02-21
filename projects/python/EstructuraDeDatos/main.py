import random

print("Random Number Game ")

vidas = 5

modo_de_juego = input("Entre la dificultad que desea ( |F| Fácil - |D| dificil ): ")

valor_computadora = random.randint(1, 100)
valor_usuario = int(input("Entre un valor del 1 al 100: "))


if modo_de_juego == 'D' or modo_de_juego == 'd':
    vidas = 3



if valor_usuario < valor_computadora:
    print("El valor es bajo.")
    vidas -= 1
elif valor_usuario > valor_computadora:
    print("El valor es mayor.")
    vidas -= 1

print("Vidas: " , vidas)
    