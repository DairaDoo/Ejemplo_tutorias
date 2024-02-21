def verificar_parentesis( cadena ):
    """Esta funcion busca los valores pares e impares en una lista."""
    parentesisIzquierdo = 0
    parentesisDerecho = 0
    
    listaParentesis = list(cadena) # convertimos la cadena en una lista.
    
    for parentesis in listaParentesis:
        if parentesis == '(':
            parentesisIzquierdo += 1
        elif parentesis == ')':
            parentesisDerecho += 1
        else:
            print("Error, el elemento no es un paréntesis.")
            
    def devolver_pares_e_impares(parentesisIzquierdo, parentesisDerecho):
        """Esta función devuelve los valores pares e impares del resultado."""
        
        if parentesisIzquierdo != 0 and parentesisDerecho != 0:
            totalPares = (parentesisIzquierdo + parentesisDerecho) / 2
            totalImpares = (parentesisIzquierdo + parentesisDerecho) % 2
            print(f"Numeros pares: {round(totalPares)} | Numeros impares: {totalImpares}.")
        
        elif parentesisIzquierdo == 0 or parentesisDerecho == 0:
            if parentesisIzquierdo > 0 and parentesisDerecho == 0:
                print(f"Numeros pares 0 | Numeros impares: {parentesisIzquierdo}")
                return
            if parentesisDerecho > 0 and parentesisIzquierdo == 0:
                print(f"Numeros pares 0 | Numeros impares: {parentesisDerecho}")
                return
    
    
    if parentesisDerecho == parentesisIzquierdo:
        devolver_pares_e_impares(parentesisIzquierdo, parentesisDerecho)
        return True
    else:
        devolver_pares_e_impares(parentesisIzquierdo, parentesisDerecho)
        return False
    
resultado = verificar_parentesis(input("Entre los parentesis: ")) # llamamos nuestra función.
print(resultado)