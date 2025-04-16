#class Clase1:
    #def metodo1(self):
        #print("Hola soy el metodo de la clase 1")

#class Clase2:
    #def metodo2(self):
        #print("Hola soy el metodo de la clase 2")
    
#class Clase3(Clase1, Clase2):

    #def metodo3(self):
        #print("Hola soy el metodo de la clase 3")

#c = Clase3()
#c.metodo1()


class Volador:
    def __init__(self, volar):
        self.volar = volar
        print("Estoy volando")

class Nadador:
   def __init__(self, nadar):
       self.nadar = nadar
       print("Estoy nadando")
    
class Pato(Volador, Nadador):
    def __init__(self, volar, nadar):
        Volador.__init__(self, volar)
        Nadador.__init__(self, nadar)
       
pato1 = Pato("Yo puedo volar", "Y tambien se nadar")
print(pato1.volar)
print(pato1.nadar)

