class Gato:
    adoptado = 'True'

    def __init__(self, nombre, raza, color, ident):

        #Atributos de la instacia
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.ident = ident

    def correr(self):
        print('{} corre.'.format(self.nombre))

    def dormir(self):
        print('{} duerme.'.format(self.nombre))

    def genero(self, ident):
        sexo = dict( { 1: 'Macho', 2: 'Hembra' } )
        if ident in sexo:
            print('{} es {}'.format(self.nombre, sexo.get(ident))) 
        else:
            print('Desconocido')

# Creación de objetos con sus atributos
gato1 = Gato('Orion', 'Gato europeo', 'blanco', 1)
gato2 = Gato('Eizen', 'Gato común', 'negro', 2)

# Acceso a los atributos de la instancia
print('{} es de raza {} de color {}'.format(gato1.nombre, gato1.raza, gato1.color))
print('{} es de raza {} de color {}'.format(gato2.nombre, gato2.raza, gato2.color))

# Llamda a los métodos
gato1.correr()
gato2.dormir()
gato1.genero(gato1.ident)
gato2.genero(gato2.ident)