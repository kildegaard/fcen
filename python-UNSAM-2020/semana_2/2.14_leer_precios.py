# Ejercicio 2.14 - Diccionario como contenedor

import csv
import sys
from pprint import pprint


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
        data = csv.reader(file)
        dictio = {}
        for line in data:
            try:
                dictio[line[0]] = float(line[1])
            except IndexError:
                print('Problemillas!')
    pprint(dictio)
    return dictio


def main(argumentos):
    if len(argumentos) == 2:
        nombre_archivo = argumentos[1]
    else:
        nombre_archivo = '../Data/precios.csv'

    precios = leer_precios(nombre_archivo)
    return precios


if __name__ == '__main__':
    precios = main(sys.argv)
