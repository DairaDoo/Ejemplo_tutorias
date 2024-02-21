archivo = open("datos.txt", "r")

while True:
    linea = archivo.readline() # leer cada linea del archivo.
    
    if not linea: # si el archivo no tiene información, se finaliza el ciclo.
        break
    
    print(f"Nueva linea ==> {linea}")
    