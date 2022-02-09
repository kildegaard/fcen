# Ejercicio 2.12 - Lista de tuplas

import csv
import sys


def leer_camion(nombre_archivo):
    '''
    Esta función levanta un .csv y devuelve la misma
    en forma de list de tuplas.
    '''
    with open(nombre_archivo, 'rt') as file:
        next(file)
        data = csv.reader(file)
        lista_datos = []
        cont_lineas_na = 0
        for line in data:
            try:
                lista_datos.append((line[0], int(line[1]), float(line[2])))
            except:
                cont_lineas_na += 1
    print(lista_datos)

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
