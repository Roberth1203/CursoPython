import Core

print('***************************************************')
print('|            Calculadora básica Python            |')
print('***************************************************')
print('\n')
print('Por favor, ingrese alguna de las opciones listadas:')
print('1. Suma')
print('2. Resta')
print('3. Producto')
print('4. División')


tipo = int(input('Indique que operación quiere realizar: '))
num1 = float(input('Ingrese el primer número (puede llevar decimales): '))
num2 = float(input('Ingrese el segundo número (puede llevar decimales): '))

calc = Core.Calculos(tipoOperacion = tipo, numeroA = num1, numeroB = num2)
calc.calcular()