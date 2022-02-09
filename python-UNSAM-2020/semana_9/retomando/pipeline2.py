# ej 9.9

from vigilante import vigilar
import csv

file = 'mercadolog.csv'
lineas = vigilar(file)

filas = csv.reader(lineas)

for fila in filas:
    print(fila)
