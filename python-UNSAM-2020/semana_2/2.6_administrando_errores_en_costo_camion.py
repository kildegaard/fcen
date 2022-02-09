# Ejericio 2.6 - Administrando errores en costo_camion
import sys
import csv


def costo_camion(archivo_entrada):
    '''
    Función que recibe un archivo .csv con información sobre
    cajones de fruta: [Fruta cant_cajas precio_cajas] y devuelve
    el costo total de las mismas
    '''
    # archivo_entrada = '../Data/camion.csv'

    with open(archivo_entrada, 'rt') as file:
        # Leo el archivo y lo guardo temporalmente en variable data
        data = csv.reader(file)
        # Separo el header para que no me moleste
        headers = next(file)

        # Acá se hace la cuenta en sí
        costo_total = 0
        problemas = False
        problemas_lista = []
        for row in data:
            try:
                costo_total += int(row[1]) * float(row[2])
            except ValueError:
                problemas = True
                problemas_lista.append(row[0])
    if problemas == True:
        print('Hubo problemas en el/los siguiente/s elemento/s: ', end='')
        # for fruta in problemas_lista:
        #     print(fruta, end=' | ')
        print(*problemas_lista, sep=' | ')
    else:
        print('Todo OK!')

    return costo_total


def main(argumentos):
    # Función principal del programa

    # Guardo la info del path del .csv
    archivo_entrada = argumentos[0]

    # Se llama a la función que hace la cuenta
    valor_costo = costo_camion(archivo_entrada)

    print(f'Valor del costo final: ${valor_costo:.2f}.-')


# INICIO DE EJECUCIÓN DEL PROGRAMA
if __name__ == '__main__':
    # Le paso [1:] al sys.argv para no guardar el nombre del archivo .py
    main(sys.argv[1:])
