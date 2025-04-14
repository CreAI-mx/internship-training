from abc import ABC, abstractmethod
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.2 

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, str, salario_base, float, horas_trabajadas: int):
        super().__init__(nombre, salario_base)
        self.nombre = nombre
        self.salario_base = salario_base
        self.str = str
        self.float = float
        self.horas_trabajadas = horas_trabajadas
  
    def calcular_salario(self):
        return self.salario_base * self.horas_trabajadas
    
empleado_TC = EmpleadoTiempoCompleto("Luis", 5000) 
empleado_PH = EmpleadoPorHora("Ana", 150, 40)

print(f"Salario de {empleado_TC.nombre}: {empleado_TC.calcular_salario()}")
print(f"Salario de {empleado_PH.nombre}: {empleado_PH.calcular_salario()}")
