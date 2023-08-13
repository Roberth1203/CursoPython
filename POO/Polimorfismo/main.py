class Persona:
    def __init__(self, nacionalidad, edad, nombre):
        self.nacion = nacionalidad
        self.edad = edad
        self.nombre = nombre

    def mostrarAtributos(self):
        print('[{}] -> Nacionalidad: {}, Edad: {} años, Nombre: {}'.format('Persona', self.nacion, self.edad, self.nombre))

class Hombre(Persona):
    def __init__(self, nacionalidad, edad, nombre):
        self.nacion = nacionalidad
        self.edad = edad
        self.nombre = nombre

    def mostrarAtributos(self):
        print('[{}] -> Nacionalidad: {}, Edad: {} años, Nombre: {}'.format('Hombre', self.nacion, self.edad, self.nombre))

class Mujer(Persona):
    def __init__(self, nacionalidad, edad, nombre):
        self.nacion = nacionalidad
        self.edad = edad
        self.nombre = nombre

    def mostrarAtributos(self):
        print('[{}] -> Nacionalidad: {}, Edad: {} años, Nombre: {}'.format('Mujer', self.nacion, self.edad, self.nombre))


obj1 = Persona('Mexicana', 45, 'Romulo')
obj2 = Hombre('Alemana', 18, 'Jurgen')
obj3 = Mujer('Francesa', 23, 'Marie')

obj1.mostrarAtributos()
obj2.mostrarAtributos()
obj3.mostrarAtributos()