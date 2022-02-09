# Ejercicio 2.5 - Transformar un script en una función
import sys
import informe_funciones as informe


def costo_camion(archivo_entrada):
    # archivo_entrada = '../Data/camion.csv'

    camion = informe.leer_camion(archivo_entrada)
    costo_total = 0
    for elemento in camion:
        costo_total += elemento['cajones'] * elemento['precio']

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
