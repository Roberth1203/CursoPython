class Engine:

    def __init__(self, name):
        self.name = name

    def WriteText(self, innerText, newLine):
        ''' Agrega contenido al archivo especificado\n
            Argumentos:\n
            innerText = Texto que se desea agregar\n
            newLine = Especifica si es necesario agregar un salto de línea al final del texto\n
        '''
        try:
            print('Creando archivo [{}] con el texto: {}'.format(self.name, innerText))
            file = open(self.name, 'a')
            if (newLine):
                file.write('{}\n'.format(innerText))
            else:
                file.write('{}'.format(innerText))
        except:
            print('Error de escritura del archivo.')
        finally:
            file.close()
            
    # def ReadFile(self):
    #     ''' Imprime el contenido del archivo especificado'''
    #     try:
    #         file = open(self.name, 'r', encoding='utf-8')
    #         print(file.read())
    #     except:
    #         print('Error de lectura de archivo')
    #     finally:
    #         file.close()
