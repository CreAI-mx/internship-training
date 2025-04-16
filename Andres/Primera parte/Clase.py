class Producto:
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    def calcular_precio_con_impuesto(self):
        # Calcula el precio con impuesto (16%)
        return self.precio_base * 1.16

    def aplicar_promocion(self, monto, porcentaje=False):
        # Aplica la promoción al precio base
        if porcentaje:
            if 0 <= monto <= 100:
                self.precio_base -= self.precio_base * (monto / 100)
            else:
                raise ValueError("El monto porcentual debe estar entre 0 y 100.")
        else:
            if 0 <= monto <= self.precio_base:
                self.precio_base -= monto
            else:
                raise ValueError("El monto en pesos debe estar entre 0 y el precio base.")

# Ejemplo de uso:
producto = Producto("Zapatos deportivos", 1500)
print(f"Precio con impuesto: ${producto.calcular_precio_con_impuesto():.2f}")

# Aplicar una promoción del 20%:
producto.aplicar_promocion(20, porcentaje=True)
print(f"Precio base después de la promoción: ${producto.precio_base:.2f}")

# Aplicar una promoción de $300:
producto.aplicar_promocion(300, porcentaje=False)
print(f"Precio base después de la promoción: ${producto.precio_base:.2f}")


class Libro:
    @staticmethod
    def es_publicado_en_mexico(isbn):
        try:
            # Dividir el ISBN en grupos usando el guion como separador
            grupos = isbn.split('-')
            # Validar si el ISBN contiene al menos 4 grupos y el segundo grupo es "607"
            if len(grupos) == 4 and grupos[1] == "607":
                return True
            return False
        except Exception as e:
            print(f"Error al analizar el ISBN: {e}")
            return False

# Ejemplo de uso
isbn_mexicano = "978-607-02-2034"
isbn_otro = "978-981-02-2034"

print(Libro.es_publicado_en_mexico(isbn_mexicano))  # Devuelve True
print(Libro.es_publicado_en_mexico(isbn_otro))     # Devuelve False


class Carro:
    ruedas = 4 
    def __init__(self, marca, kilometros, anio):
        self.marca = marca
        self.kilometros = kilometros
        self.anio = anio
        print(f"Se ha creado un auto {self.marca} con 200 kilometros")

    def __del__(self):
        print(f"Se ha vendido el auto {self.marca} con {self.kilometros} kilometros")
    def __str__(self):
        return "El auto es un {}, tiene {} kilometros y es del anio {}". format(self.marca, self.kilometros, self.anio)
    
miCarro = Carro("Audi", 200, 2012)

print(str(miCarro))

