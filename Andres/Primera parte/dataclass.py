from dataclasses import dataclass

class Producto:
    def __init__(self, nombre, precio, GTIN):
        self.nombre = nombre
        self.precio = precio
        self.GTIN = GTIN    
    
    def __eq__(self, other):
        @dataclass
    
        class Rectangulo:
            base: float
            altura: float
        
        def __eq__(self, other):
            return(self.base == other.base and self.altura == other.altura) 
        
        @property
        def area(self):
            return self.base * self.altura
        @property
        def perimetro(self):
            return 2 * (self.base + self.altura)    
        
        rect1 = Rectangulo(2, 3)
        rect2 = Rectangulo(3, 2)
        print(rect1.area)
        print(rect1.perimetro)
        print(rect2.area)
        print(rect2.perimetro) 
               