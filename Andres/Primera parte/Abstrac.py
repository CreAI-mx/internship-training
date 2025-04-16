from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def saltar(self):
        pass

class Rana (Animal):
    def saltar(self):
        print("La rana ha dado un salto de metros")

class Elefante(Animal):
    def saltar(self):
        print("El elefante no puede saltar")

rana = Rana()
rana.saltar()

elefante = Elefante()
elefante.saltar()
