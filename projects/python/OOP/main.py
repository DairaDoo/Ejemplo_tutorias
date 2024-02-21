class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacer_sonido(self):
        return "Algo"
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
mi_animal = Animal("Algo")
mi_perro = Perro("Perro")
mi_gato = Gato("Gato")

print(mi_animal.hacer_sonido())
print(mi_perro.hacer_sonido())
print(mi_gato.hacer_sonido())