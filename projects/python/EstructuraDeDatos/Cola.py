class Cola:
    def __init__(self):
        self.items = []
    
    # Verifica si la lista está vacía 
    def is_empty(self):
        return len(self.items) == 0
    
    # Verifica la cantidad de elementos en la lista
    def size(self):
        return len(self.items)
    
    def enqueue(self, elemento):
        self.items.append(elemento)
    
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
item = []

lista_Cola = Cola()

lista_Cola.enqueue("Auto Toyota")
lista_Cola.enqueue("Auto Subaru")
lista_Cola.enqueue("Auto Porche")
lista_Cola.enqueue("Auto Mitsubishi")
lista_Cola.enqueue("Auto Jeep")
lista_Cola.enqueue("Auto Nissan")
lista_Cola.enqueue("Auto Ford")

print("Cola", lista_Cola.items)
print("Tamaño de la cola: ", lista_Cola.size())
print("Elemento retirado: ", lista_Cola.dequeue())
print("Cola después de dequeue: ", lista_Cola.items)
print(lista_Cola.is_empty())
print("Elemento en la parte frontal de la cola: ", lista_Cola.peek())