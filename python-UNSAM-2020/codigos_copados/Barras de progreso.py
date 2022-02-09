from progress.counter import Countdown
import time
from progress.spinner import Spinner
from progress.bar import Bar, ChargingBar
import os
import time
import random

# Declara un objeto de la clase Bar(). En cada ciclo la barra
# muestra una porción hasta llegar a su máxima longitud en el
# ciclo 20. La barra se representa con el carácter #

bar1 = Bar('Procesando:', max=20)
for num in range(20):
    time.sleep(0.2)
    bar1.next()
bar1.finish()


# Declara un objeto de la clase ChargingBar(). Cuando comienza
# el bucle aparece una barra punteada y durante los ciclos los
# puntos "∙" son sustituidos por el carácter "█" hasta alcazar
# el 100%.

bar2 = ChargingBar('Instalando:', max=100)
for num in range(100):
    time.sleep(random.uniform(0, 0.2))
    bar2.next()
bar2.finish()


# Declara un objeto de la clase Bar(). En cada ciclo la barra
# muestra el carácter del atributo "fill" (·) hasta alcanzar
# el 100%.
# Durante el proceso se escribe un archivo de texto con
# 5000 caracteres ('X' y 'O') que son generados por una función
# aleatoria. En este caso el retardo de tiempo es real.
# En el módulo hay otras clases para declarar objetos similares:
# FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar
# y ShadyBar

bar3 = Bar('Escribiendo:', fill='·', suffix='%(percent)d%%')
caracteres = ['X', 'O']
datos = os.getcwd()+os.sep+"datos.txt"
archivo = open(datos, "w")
for i in range(100):
    cadena = ""
    longitud = 5000
    for num in range(longitud):
        cadena += caracteres[random.randint(0, 1)]

    archivo.write(cadena + "\n")
    bar3.next()

bar3.finish()
archivo.close


# Declara un objeto de la clase Spinner(). En cada ciclo una hélice
# gira hasta que se completa la lectura del archivo creado en el
# ejemplo anterior. Cuando se completa la lectura se muestra el
# número total de caracteres encontrados de cada tipo ('X'/'O').
# Una hélice muestra que un proceso se está ejecutando pero no
# no ayuda a prever su final.
# El módulo tienes otras clase para declarar objetos similares:
# PieSpinner, MoonSpinner, LineSpinner y PixelSpinner.


spinner = Spinner('Leyendo: ')
cuenta_X = 0
cuenta_O = 0
archivo = open(datos, "r")
while True:
    linea = archivo.readline()
    if linea:
        for caracter in linea:
            if caracter == 'X':
                cuenta_X += 1
            elif caracter == 'O':
                cuenta_O += 1
    else:
        break
    time.sleep(0.1)
    spinner.next()

print(' X=', cuenta_X, 'O=', cuenta_O)
archivo.close


# Declara un objeto de la clase Countdown(). En cada ciclo un
# contador que comienza en 100 va disminuyendo su valor hasta
# alcanzar 0, que marca el fin del bucle.
# El módulo tiene otras clases para declarar objetos
# similares: Counter, Pie y Stack


contador = Countdown("Contador: ")
for num in range(100):
    contador.next()
    time.sleep(0.05)

print()
