class Persona:
    def __init__(self, nombre, edad,  apellido, sexo):
        self.nombre = nombre
        self. edad = edad
        self. apellido = apellido
        self. sexo = sexo

    def datosPersonales(self):
     print(f"El nombre de la persona es: {self.nombre}")
     print(f"La edad de la persona es: {self.edad}")
     print(f"El apellido de la persona es: {self.apellido}")
     print(f"El sexo de la persona es: {self.sexo}")

miPersona = Persona("Andres", 22, "Lampon", "Masculino")
miPersona. datosPersonales()

print("********")
class Empleado(Persona):
   def datosEmpleado(self, vacaciones, salario):
      print(f"Su dias de vacaciones son: {vacaciones}")
      print(f"Su salario es: {salario}")

miEmpleado = Empleado("Cinita", 22, "Lampon", "Femenino")
miEmpleado.datosPersonales()
miEmpleado.datosEmpleado(30, 5000)


