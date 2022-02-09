#!/usr/bin/env python3

import sys


def costo_camion(archivo_entrada):
    # archivo_entrada = '../Data/camion.csv'

    with open(archivo_entrada, 'rt') as file:
        headers = next(file)

        data = []
        for linea in file:
            data.append(linea.strip().split(','))

    costo_total = 0
    for elemento in range(len(data)):
        costo_total += int(data[elemento][1]) * float(data[elemento][2])

    # print(f'Costo total: $ {costo_total:.2f}.-')
    return costo_total


def main(argumentos):
    try:
        archivo_entrada = argumentos[1]
        valor_costo = costo_camion(archivo_entrada)
        print(f'Valor del costo final: ${valor_costo:.2f}')
    except IndexError:
        print(f'No se pasó ningún archivo!')
        print(f"{argumentos[0]} 'PATH/A/CAMION.CSV'")


if __name__ == '__main__':
    main(sys.argv)
