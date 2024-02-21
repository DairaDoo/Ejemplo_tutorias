def verificar_parentesis(cadena):
    """Esta funcion busca los valores pares e impares en una lista."""
    CantidadParentesisIzquierdo = 0
    CantidadParentesisDerecho = 0
    
    def devolver_pares_e_impares(parentesisIzquierdo, parentesisDerecho):
        """Esta función devuelve los valores pares e impares del resultado."""
        totalPares = min(parentesisIzquierdo, parentesisDerecho)
        totalImpares = abs(parentesisIzquierdo - parentesisDerecho)
        print(f"Números pares: {totalPares} | Numeros impares: {totalImpares}.")
    
    listaParentesis = list(cadena)  # Convertimos la cadena en una lista.
    
    for parentesis in listaParentesis:
        if parentesis == '(':
            parentesisIzquierdo += 1
        elif parentesis == ')':
            parentesisDerecho += 1
        else:
            print("Error, el elemento no es un paréntesis.")
            
    if parentesisDerecho == CantidadParentesisIzquierdo:
        devolver_pares_e_impares(CantidadParentesisIzquierdo, CantidadParentesisDerecho)
        return True
    else:
        devolver_pares_e_impares(CantidadParentesisIzquierdo, CantidadParentesisDerecho)
        return False
    
resultado = verificar_parentesis("()()()))")
