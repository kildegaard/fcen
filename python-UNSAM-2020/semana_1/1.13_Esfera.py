# Ejercicio 1.13 - El volumen de una esfera

import math

print("Cálculo del volumen de la esfera de radio r")
radio = float(input('Ingrese el radio: '))
print('El volumen de la esfera de radio {:.2f} es {:.2f}'.format(radio, 4./3 * math.pi * radio ** 3))
