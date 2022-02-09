# Ejericio 2.6 - Administrando errores

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

'''
Salida por consola
==================

PS D:\gitLab\pyunsam\Semana 2> python -i .\2.6_administrando_errores.py
>>> preguntar_edad('Gustavo')
ingresá tu edad Gustavo: 32
32
>>> preguntar_edad('Gustavo')
ingresá tu edad Gustavo: -1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".\2.6_administrando_errores.py", line 6, in preguntar_edad
    raise ValueError('La edad no puede ser negativa.')
ValueError: La edad no puede ser negativa.
'''

for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingesó una edad válida.')

'''
Salida por Consola
==================

PS D:\gitLab\pyunsam\Semana 2> python -i .\2.6_administrando_errores.py
ingresá tu edad Pedro: 40
Pedro tiene 40 años.
ingresá tu edad Juan: -10
Juan no ingesó una edad válida.
ingresá tu edad Caballero: Alf
Caballero no ingesó una edad válida. 
'''