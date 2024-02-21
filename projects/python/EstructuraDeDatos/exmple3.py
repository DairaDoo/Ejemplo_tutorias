def ejercicio_6(lista): 
    for i in range(len(lista)): #O(n)
        for j in range(i+1, len(lista)): #O(n)
            if lista[i] > lista[j]: #O(1)
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [9,2,3,4,5,6]

print(ejercicio_6(lista))