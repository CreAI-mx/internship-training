from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def procesarFormas(lista_formas):
        for forma in lista_formas:
            print(f"Área: {forma.area()}")
            print(f"Perímetro: {forma.perimetro()}")

    
class Rectangulo (Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def procesarFormas(lista_formas):
        for forma in lista_formas:
            print(f"Area: {forma.area()}")
            print(f"Perímetro: {forma.perimetro()}")

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

Lista_formas = [circulo, rectangulo]
Rectangulo.procesarFormas(Lista_formas)
Circulo.procesarFormas(Lista_formas)


from abc import ABC, abstractmethod

class Empleado(ABC):
     def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
        
        @abstractmethod
        def calcular_salario(self):
            pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono_mensual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_mensual = bono_mensual
        self.apellido = apellido
    
    def calcular_salario(self):
        return self.salario_base + self.bono_mensual

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido,  salario_base, horas_trabajadas, bono_horas):
        super().__init__(nombre, apellido, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.bono_horas = bono_horas
        self.apellido = apellido


    def calcular_salario(self):
        return self.salario_base * self.horas_trabajadas + self.bono_horas
    
    def procesar_empleados(lista_empleados):
        for empleado in lista_empleados:
            print(f"Empleado: {empleado.nombre} {empleado.apellido} : {empleado.calcular_salario()} MXN")
    
empleado_TC = EmpleadoTiempoCompleto("Oscar", "Essau", 5000, 1000)
print(f"Salario de {empleado_TC.nombre}, {empleado_TC.apellido}, {empleado_TC.calcular_salario()}")

empleado_ph = EmpleadoPorHora("Jessica", "Puente",  20, 40, 200)
print(f"Salario de {empleado_ph.nombre}, {empleado_ph.apellido}, {empleado_ph.calcular_salario()}")

empleados = [empleado_TC, empleado_ph]
EmpleadoPorHora.procesar_empleados(empleados)
Empleado.procesar_empleados(empleados)
Empleado.procesar_empleados(empleados)
