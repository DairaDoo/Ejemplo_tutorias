suma = lambda x, y: x + y
resta = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y

opciones = ['s', 'r', 'm', 'd', '0']

while True:
    procesoMat = input("Escoge una: 's' > sumar | 'r' > restar | 'm' > multiplicar | 'd' > dividir | '0' >  finalizar el programa: ").lower()
    
    
    if procesoMat == '0':
        print("Programa Finalizado. Gracias por usar.")
        break
    elif procesoMat not in opciones:
        print("Opción Inválida!")
        continue
    
    
    x = int(input("Entre el primer valor: "))
    y = int(input("Entre el segundo valor: "))
    
    if procesoMat == 's':
        print(f"Suma: {suma(x,y)}")
    
    elif procesoMat == 's':
        print(f"Resta: {resta(x,y)}")
    
    elif procesoMat == 's':
        print(f"Multiplicación: {mult(x,y)}")
        
    elif procesoMat == 'd':
        if y == 0:
            print("Error | No es posible dividir entre 0.\n")
            continue
            
        print(f"División: {div(x,y)}")
        