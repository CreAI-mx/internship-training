from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(animal):
    def hacer_sonido(self):
        return "Miau!"  
perro = Perro()
print(perro.hacer_sonido()) 

gato = Gato()
print(gato.hacer_sonido())



from abc import ABC, abstractmethod

class animal(ABC):
    @property
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(animal):
    def hacer_sonido(self):
        return "Miau!"  
perro = Perro()
print(perro.hacer_sonido()) 

gato = Gato()
print(gato.hacer_sonido())



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.nombre = nuevo_nombre
p = Persona("Ana")
p.nombre = "Andrea"
print(p.nombre)


