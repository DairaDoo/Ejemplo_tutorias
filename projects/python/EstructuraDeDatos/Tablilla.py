# Clase para representar una tablilla de automóvil de Puerto Rico
class Tablilla:
    def __init__(self, numero, letra):
        self.numero = numero
        self.letra = letra

    def __str__(self):
        return f"{self.letra}-{self.numero}"

# Modificar la clase Cola para trabajar con tablillas
class Cola:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, tablilla):
        self.items.append(tablilla)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

# Crear una cola de tablillas
cola_tablillas = Cola()

# Añadir tablillas a la cola
cola_tablillas.enqueue(Tablilla("1234", "HJM"))
cola_tablillas.enqueue(Tablilla("5678", "FTS"))
cola_tablillas.enqueue(Tablilla("9012", "CTD"))

# Realizar operaciones con la cola
print("Cola de tablillas:", [str(tablilla) for tablilla in cola_tablillas.items])
print("Tamaño de la cola:", cola_tablillas.size())
print("Tablilla retirada:", cola_tablillas.dequeue())
print("Cola después de dequeue:", [str(tablilla) for tablilla in cola_tablillas.items])
print("¿La cola está vacía?", cola_tablillas.is_empty())
print("Tablilla en la parte frontal de la cola:", cola_tablillas.peek())