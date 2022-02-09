# Ejercicio 2.18 - Un ejemplo práctico de enumerate()

import csv

def leer_camion(archivo_entrada):
    with open(archivo_entrada, 'rt') as file:
        next(file)
        data = csv.reader(file)

        for n_line, line in enumerate(data, start = 1):
            try:
                valor = int(line[1]) * float(line[2])
                # print(line)
            except ValueError:
                print(f'La fila {n_line} no se pudo interpretar. ')
                print(f'{line}')

    

archivo_entrada = '../Data/missing.csv'
leer_camion(archivo_entrada)