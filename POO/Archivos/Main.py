from Core import Engine as engine

print('***********************************')
print('***** Trabajando con archivos *****')
print('***********************************')
print('\n')
print('Por favor, ingrese los siguientes datos:')
nombre = print(input('Nombre del archivo: '))

archivo = engine(name= nombre)
archivo.WriteText('prueba', 'False')