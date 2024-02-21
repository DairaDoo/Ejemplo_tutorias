print("Creando archivo...")

archivo = open("datos.txt", "a") 

print("Escribiendo en el archivo....")
archivo.write("Este texto será puesto en el archivo.\n")

for i in range(1, 11):
    archivo.write(f"Line #{i}\n")

print("Fin de los comandos con archivos.")
archivo.close()