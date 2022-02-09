# Ejercicio 2.13 - Lista de diccionarios

import csv
import sys
from pprint import pprint


def leer_camion(nombre_archivo):
    '''
    Esta función levanta un .csv y devuelve la misma
    en forma de list de tuplas.
    '''
    with open(nombre_archivo, 'rt') as file:
        next(file)
        data = csv.reader(file)
        lista_de_dict = []
        cont_lineas_na = 0
        for line in data:
            try:
                dictio = {
                    'nombre': line[0],
                    'cajones': int(line[1]),
                    'precio': float(line[2])
                }
                lista_de_dict.append(dictio)
            except:
                cont_lineas_na += 1
    pprint(lista_de_dict)

    if cont_lineas_na != 0:
        print(f'Hubo un total de {cont_lineas_na} productos con problemas.')


def main(argumentos):
    # Guardo la info del path del .csv
    if len(argumentos) == 2:
        nombre_archivo = argumentos[1]
    else:
        nombre_archivo = '../Data/camion.csv'
    # Ejecuto mi función
    leer_camion(nombre_archivo)


if __name__ == '__main__':
    main(sys.argv)
