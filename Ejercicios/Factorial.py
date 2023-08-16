print('*** Generar factorial ***')
number = int(input('Ingrese el número para consultar el factorial: '))

def factorial(n):
    if n == 1:
        return n
    else:
        return  n * factorial(n-1)

print(factorial(number))