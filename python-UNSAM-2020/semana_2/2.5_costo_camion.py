# Ejercicio 2.5 - Transformar un script en una función
import sys


def costo_camion(archivo_entrada):
    # archivo_entrada = '../Data/camion.csv'

    with open(archivo_entrada, 'rt') as file:
        headers = next(file)

        data = []
        for linea in file:
            # print(repr(linea))
            lin_aux1 = linea.strip()
            # print(repr(lin_aux1))
            lin = lin_aux1.split(',')
            # print(lin)
            data.append(lin)

    costo_total = 0
    for elemento in range(len(data)):
        costo_total += int(data[elemento][1]) * float(data[elemento][2])

    # print(f'Costo total: $ {costo_total:.2f}.-')
    return costo_total


def main(argumentos):
    if argumentos:
        archivo_entrada = argumentos[0]
    else:
        archivo_entrada = '../Data/camion.csv'

    valor_costo = costo_camion(archivo_entrada)

    print(f'Valor del costo final: ${valor_costo:.2f}')


if __name__ == '__main__':
    main(sys.argv[1:])
