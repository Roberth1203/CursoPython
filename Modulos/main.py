import SayHello as saludos
import datetime
from datetime import time as tiempo

saludos.saludar('Roberto')
print(datetime.datetime.now())

# Módulo datetime
fecha = datetime.datetime(1990,8,1)
print(fecha)
print(fecha.strftime('%B'))
print(fecha.strftime('%A'))

# Módulo Math
import math
radio = 10
print('Cálculo del área y circunferencia de un círculo.')
print('Área: ', round(math.pi * radio ** 2))
print('Circunferencia: ', round(2 * math.pi * radio))


# Módulo Random