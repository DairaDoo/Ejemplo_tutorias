import random # computadora escoge un valor.

randomNumber = random.randint(1, 10) # escoge un valor del 1 al 10.

number = -1 # inicializamos number.

while number != randomNumber: # mientras el numero sea diferente del randomNumber, sigue repitienote.
    number = int(input("Indique un número: ")) # pedimos un nuevo valor para number.
    if (number > randomNumber):
        print("El numero es mayor al entrado.") # el numero es mayor a randomNumber.
    elif (number < randomNumber):
        print("El número es menor al entrado.") # el numero es menor a randomNumber.
    else:
        print("Ese es el número buscado. :)") # El número es igual a randomNumber.

