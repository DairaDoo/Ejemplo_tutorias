precioProducto = [] # lista que recibirá los productos

for i in range(1, 5):
    precio = float(input(f"Entre el precio del producto #{i}: "))
    precioProducto.append(precio)


membresia = input("Entre el tipo de membresia ('plus' / 'regular'): ")

if membresia == 'plus':
    descuento = 0.20
elif membresia == 'regular':
    descuento = 0.05
else:
    print('Error ( opción inválida )')
    
print("")
    
    