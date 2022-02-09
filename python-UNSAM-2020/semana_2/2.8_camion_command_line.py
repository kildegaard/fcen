# Ejercicio 2.5 - Transformar un script en una función
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
        print(*problemas_lista, sep=' | ')
    else:
        print('Todo OK!')

    return costo_total


def main(argumentos):
    '''
    Función principal del programa
    '''

    # Guardo la info del path del .csv
    if len(argumentos) == 2:
        archivo_entrada = argumentos[1]
    else:
        archivo_entrada = '../Data/camion.csv'

    # Se llama a la función que hace la cuenta
    valor_costo = costo_camion(archivo_entrada)

    print(f'Valor del costo final: ${valor_costo:.2f}.-')


# INICIO DE EJECUCIÓN DEL PROGRAMA
if __name__ == '__main__':
    main(sys.argv)


'''
OUTPUT
======
PS D:\gitLab\pyunsam\Semana 2> python .\2.8_costo_camion_con_parametros.py
Todo OK!
Valor del costo final: $47671.15.-
PS D:\gitLab\pyunsam\Semana 2> python .\2.8_costo_camion_con_parametros.py '../Data/camion.csv'Todo OK!
Valor del costo final: $47671.15.-
PS D:\gitLab\pyunsam\Semana 2> python .\2.8_costo_camion_con_parametros.py '../Data/missing.csv'
Hubo problemas en el/los siguiente/s elemento/s: Mandarina | Naranja
Valor del costo final: $30381.15.-
'''
