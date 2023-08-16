print('*** Calculadora básica en Python ***')
print('Operacioens disponibles:\n1.- Suma\n2.- Resta\n3.- Producto\n4.- División')
option = int(input('Indique la operación a realizar: '))
number1= float(input('Número 1: '))
numero2= float(input('Número 2: '))

suma = lambda x, y:  x + y
resta = lambda x, y:  x - y
producto = lambda x, y:  x * y
division = lambda x, y:  x / y

def operaciones():
    if option == 1:
        print('La suma de {} + {} = {}'.format(number1, numero2, suma(number1, numero2)))
    elif option == 2:
        print('La resta de {} - {} = {}'.format(number1, numero2, resta(number1, numero2)))
    elif option == 3:
        print('El producto de {} * {} = {}'.format(number1, numero2, producto(number1, numero2)))
    elif option == 4:
        print('La división de {} / {} = {}'.format(number1, numero2, division(number1, numero2)))
    else:
        print('Opción no válida.')

operaciones()