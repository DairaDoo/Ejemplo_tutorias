paises = ['Argentina', 'Brasil', 'Chile', 'Dinamarca', 'Egipto'] # creamos lista.

print(f"Paises a escoger: {paises}") # imprimimos paises en plan de oferta.

pais_escogido = input("Escoga un pais de nuestro plan de oferta: ") # pedimos al usuario escoger un pais.

pais_a_encontrar = '' # incializamos la variable que guardara el pais que deseamos encontrar

for pais in paises:
    if (pais_escogido == pais):
        print(f"{pais_escogido} se encuentra en nuestro plan de oferta.")
        pais_a_encontrar = pais # si el pais se encuentra, asignamos el pais a pais encontrado.
        
if (pais_escogido != pais_a_encontrar): # si el pais escogido es diferente al pais a encontrar, no se encuentra.
    print(f"{pais_escogido} no se encuentra en nuestro plan de oferta.")












# pais_existe = False

# for pais in paises:
#     if ( pais_escogido == pais ):
#         el_pais_existe = True
    
        
        
# if pais_existe == True:
#     print(f"{pais_escogido} existe en nuestro plan de oferta.")
# else:
#     print(f"{pais_escogido} no existe en nuestro plan de oferta.")