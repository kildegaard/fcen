# Ejercicio 2.15 - Balances

import csv
import sys
from pprint import pprint


def leer_camion(archivo_camion):
    '''
    Esta función levanta un .csv con información del costo
    de cajones de fruta y devuelve una lista de tuplas con
    dicha información.
    ('nombre', 'cajones', 'precio')
    '''
    with open(archivo_camion, 'rt') as file:
        filas = csv.reader(file)
        headers = next(filas)
        lista_camion = []
        for nfila, fila in enumerate(filas, start=1):
            try:
                lote = (fila[0], int(fila[1]), float(fila[2]))
                lista_camion.append(lote)
            except:
                print(f'LC.Error en fila {nfila} - {fila}')
    return lista_camion


def costo_camion(archivo_camion):
    '''
    Esta función levanta un .csv con información del costo
    de cajones de fruta y devuelve el costo total de la 
    operación.
    '''
    with open(archivo_camion, 'rt') as file:
        filas = csv.reader(file)
        headers = next(filas)
        costo_total = 0.0
        for nfila, fila in enumerate(filas, start=1):
            data = dict(zip(headers, fila))
            try:
                ncajones = int(data['cajones'])
                precio = float(data['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f'CC.Error en fila {nfila} - {fila}')
    return costo_total


def leer_precios(archivo_precios):
    '''
    Esta función levanta un .csv con información del precio
    de venta de los cajones de fruta y verdura
    vendidos y devuelve un diccionario con dicha información.
    '''
    with open(archivo_precios, 'rt') as file:
        filas = csv.reader(file)
        precios = {}
        for line in filas:
            try:
                precios[line[0]] = float(line[1])
            except IndexError:
                # Si encuentra una línea vacía, no quiero que haga nada.
                continue
    return precios


def balance(camion, costo_total, mercaderia_vendida):
    '''
    Función que devuelve el balance de operaciones, imprimiendo
    por pantalla lo que costó el camión, lo que se recaudó con la
    venta y la diferencia. Finalmente, informa si hubo ganancia o
    pérdida total en la operación.
    '''
    # Recaudación es el acumulador que va sumando las ganancias de la venta de frutas
    recaudacion = 0.0
    # Itero en cada elemento de la lista camión
    for producto_comprado in camion:
        # Busco si la fruta que se compró (en el camión) está en la lista de frutas
        # vendidas (precio_mercaderia).

        if producto_comprado[0] in mercaderia_vendida:
            ganancia_por_fruta = mercaderia_vendida[producto_comprado[0]
                                                    ] * producto_comprado[1]
            recaudacion += ganancia_por_fruta
    balance = recaudacion - costo_total
    print(f'Balance de la situación')
    print(
        f'Costo del camión: ${costo_total:.2f} | Recaudación: ${recaudacion:.2f} | Balance neto: ${balance:.2f}.')


def main(archivo_camion, archivo_precios):
    '''
    Función principal del programa que llama a todas las demás.
    '''
    camion = leer_camion(archivo_camion)
    costo_total = costo_camion(archivo_camion)
    precios_venta = leer_precios(archivo_precios)
    balance(camion, costo_total, precios_venta)


###### COMIENZO DEL PROGRAMA ######
if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2:
        archivo_camion = args[0]
        archivo_precios = args[1]

        # Confirmado el Nº de argumentos, largamos el programa.
        main(archivo_camion, archivo_precios)

    elif len(args) < 2:
        archivo_camion = '../Data/camion.csv'
        archivo_precios = '../Data/precios.csv'

        main(archivo_camion, archivo_precios)
    else:
        print(f'Número erróneo de argumentos!')


#### OUTPUT ####
'''
Balance de la situación
Costo del camión: $47671.15 | Recaudación: $62986.10 | Balance neto: $15314.95.
'''
#### OUTPUT ####
