# Internship Training Resources

## Semana 1

### Programación Orientada a Objetos

- [ ] Qué es POO
  - [x] Clases y Objetos
  - [x] Definición de clases
  - [x] Definición y creación de objetos
  - [x] Atributos y métodos
  - [x] Métodos mágicos (__init__, __str__, __repr__, etc.)
- [ ] 4 Pilares de POO I
  - [x] Abstracción
    - [ ] Atributos de instancia y de clase
    - [ ] Métodos de instancia
    - [ ] Métodos de clase y estáticos
  - [x] Encapsulamiento
    - [x] Atributos y métodos privados
    - [x] Propiedades @ properties
    - [ ] Dataclases
  - [x] Herencia
    - [x] Clases y métodos abstractos
    - [x] Herencia Simple y múltiple
  - [x] Polimorfismo
  - [x] Composición y agregación

#### Recursos
- [Curso Python 2020](https://www.youtube.com/watch?v=71S1WywB4cY&list=PLg9145ptuAigw5pV_DRznXdOsX19dorDs&index=2)
- [Conceptos POO en Python](https://www.geeksforgeeks.org/python-oops-concepts/)
- [Quiz](https://www.geeksforgeeks.org/quizzes/python-oops-quiz/)
- [Python Object Oriented Programming (OOP): Beginner to Pro](https://www.udemy.com/course/object-oriented-programming-with-modern-python/)
- [Documentación Oficial](https://docs.python.org/3/tutorial/classes.html)

#### Ejercicios

**Definición de clases y objetos**

Crea una clase llamada 'Persona' que tenga:
- Atributos: nombre, edad, nacionalidad
- Métodos: presentarse() que imprima "Hola, soy {nombre}, tengo {edad} años y soy de {nacionalidad}"
Crea dos objetos (instancias) de esta clase con datos diferentes y llama al método presentarse()


**Métodos mágicos**

Modifica la clase Persona del ejercicio anterior para que:
1. Al imprimir el objeto (print) muestre "Persona: {nombre}, {edad} años"
2. La representación oficial (repr) muestre "Persona('{nombre}', {edad}, '{nacionalidad}')"
3. Dos personas sean iguales (==) si tienen el mismo nombre y edad


**Abstracción**

Crea una clase 'Coche' con:
- Atributos de instancia: marca, modelo, año, kilometraje
- Atributo de clase: ruedas = 4
- Método de instancia: detalles() que devuelva un string con los detalles
- Método de clase: es_coche() que reciba un objeto y devuelva True si tiene 4 ruedas
- Método estático: es_antiguo(año) que devuelva True si el año es menor a 2010


**Encapsulamiento / Atributos privados y properties**

Crea una clase 'CuentaBancaria' con:
- Atributo privado: _saldo
- Property (propiedad) saldo que retorne el valor de _saldo
- Métodos depositar y retirar que actualicen el saldo
- Validar que no se pueda retirar más dinero del disponible


**Encapsulamiento / Dataclasses**


Usando @dataclass, crea una clase 'Producto' con:
- nombre: str
- precio: float
- stock: int = 0
- codigo: str (generado automáticamente como "PROD-{nombre}-{precio}") usa el método mágico (__post_init__)


**Herencia simple y abstracta**


Crea una estructura de clases para representar empleados:
1. Clase abstracta Empleado con:
   - Atributos: nombre, salario_base
   - Método abstracto: calcular_salario()
2. Clase EmpleadoTiempoCompleto que herede de Empleado:
   - calcular_salario(): salario_base + bono (20% del salario_base)
3. Clase EmpleadoPorHora que herede de Empleado:
   - Atributo: horas_trabajadas
   - calcular_salario(): salario_base * horas_trabajadas


**Herencia múltiple**


Crea un sistema de herencia múltiple con:
1. Clase Volador con método volar()
2. Clase Nadador con método nadar()
3. Clase Pato que herede de ambas e implemente ambos métodos


**Polimorfismo**

Crea una clase Abstracta llamada Forma con los métodos
- Método area()
- Método perimetro()
Crea una función 'procesar_formas' que reciba una lista de objetos tipo Forma:
La función debe imprimir el área y perímetro de cada objeto
Luego crea clases Circulo y Rectangulo que implementen la clase Forma


**Composición y Agregación**

Crea una clase 'Motor' con atributo 'tipo' y método 'arrancar()'
Crea una clase 'Auto' que use composición con Motor (el motor se crea al crear el auto)


**Agregación**

Crea una clase 'Estudiante' y una clase 'Curso'.
Un estudiante puede estar en varios cursos (agregación)
Implementa los métodos necesarios para agregar y obtener estudiantes de un curso, y cursos de un estudiante.


## Semana 2 Git

### Instalación y configuración

Instala git en tu OS

**Windows**

```
winget install --id Git.Git
```

**Ubuntu**

```
sudo apt install git
```


**Configura git**

Configura tu nombre e email

```
git config --global user.email "[tu email]"

git config --global user.name "[Tu nombre]"

```

#### Recursos
- [Curso Git 1 hora](https://youtu.be/VdGzPZ31ts8)
- [Curso Git extedido](https://youtu.be/3GymExBkKjE)
