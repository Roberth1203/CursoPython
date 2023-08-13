class Roberto:
    def el(self):
        print('El padre se llama José Roberto')

class Alma:
    def ella(self):
        print('La madre se llama Alma Angélica')

class Robertito(Roberto, Alma):
    def hijo(self):
        print('El hijo se llama José Roberto')

class Alejandro(Roberto, Alma):
    def bebe(self):
        print('El bebé se llama Alejandro')

# Invocación de las instancias y métodos
hijoMayor = Robertito()
hijoMenor = Alejandro()

hijoMayor.el()
hijoMayor.ella()
hijoMayor.hijo()
print(' ')
hijoMenor.el()
hijoMenor.ella()
hijoMenor.bebe()

