


class nombre:
    pass
victor = nombre()

victor.nombre = "Hola soy Victor"
victor.edad = 25
victor.sexo = "Masculino"
victor.pais = "Mexico"

print(victor.nombre)
print(victor.edad)
print(victor.pais)



class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def presentar(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}.")
persona1 = Persona("Andres", 22, "México")
persona2 = Persona("Jessica", 24, "Mexico")
persona1.presentar()
persona2.presentar()  


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def str(self):
        return(f"Persona: {self.nombre}, tengo {self.edad} años")
    def __repr__(self):
        return (f"Persona: {self.nombre}, tengo {self.edad} años, soy de nacionalidad {self.nacionalidad}")
    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

persona1 = Persona("Andres", 22, "México")
persona2 = Persona("Luis", 30, "Argentina")
persona3 = Persona("Ana", 25, "España") 

print(persona1)  
print(repr(persona1))  

print(persona1 == persona2)  
print(persona1 == persona3)

class Coche:

    ruedas = 4
    
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo 
        self.año = año 
        self.kilometraje = kilometraje

    def detalles(self):
        return f"{self.marca} {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje} km"
   
    @classmethod
    def es_coche(cls, objeto):
        
        return hasattr(objeto, "ruedas") and objeto.ruedas == cls.ruedas
   
    @staticmethod
    def es_antiguo(año):
        
        return año < 2010
    
coche1 = Coche("Toyota", "Corolla", 2005, 1000)
coche2 = Coche("Porche", "Carrera 911", 2020, 500)

#Metodo instancia
print(coche1.detalles())
print(coche2.detalles())

#Metodo estatico
print(Coche.es_antiguo(coche1.año))
print(Coche.es_antiguo(coche2.año))

#Metodo de clase
print(Coche.es_coche(coche1))
print(Coche.es_coche("esto no es un coche"))






