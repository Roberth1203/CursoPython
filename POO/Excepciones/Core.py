class Calculos:
    def __init__(self, tipoOperacion, numeroA, numeroB):
        self.tipo = tipoOperacion
        self.num1 = numeroA
        self.num2 = numeroB

    def calcular(self):
        try:
            print('-> Procesando la petición')

            if (self.tipo == 1):
                print('La suma de {} + {} es: {}'.format(self.num1, self.num2, self.num1 + self.num2))
            elif (self.tipo == 2):
                print('La resta de {} - {} es: {}'.format(self.num1, self.num2, self.num1 - self.num2))
            elif (self.tipo == 3):
                print('El producto de {} * {} es: {}'.format(self.num1, self.num2, self.num1 * self.num2))
            elif (self.tipo == 4):
                print('La división de {} / {} es: {}'.format(self.num1, self.num2, self.num1 / self.num2))
            else:
                print('La operación [{}] no se encuentra en las opciones actuales'.format(self.tipo))

        except ZeroDivisionError:
            print('No es posible realizar una division con cero, verifique los números provistos')
        except:
            print('Ocurrió un error inesperado')
        finally:
            print('-> Finaliza el proceso')