# Ejercicio 2.15 - Balances

import csv
import sys
from pprint import pprint


def leer_camion(archivo_camion):
    '''
    Esta función levanta un .csv con información del costo
    de cajones de fruta y devuelve un diccionario con dicha
    información:
    [{nombre1, cajones1, precio1}, ...].
    '''
    with open(archivo_camion, 'rt') as file:
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

    if cont_lineas_na != 0:
        print(f'Hubo un total de {cont_lineas_na} productos con problemas.')
    return lista_de_dict


def leer_precios(archivo_precios):
    '''
    Esta función levanta un .csv con información del precio
    de venta de los cajones de fruta y verdura
    vendidos y devuelve un diccionario con dicha información.
    '''
    with open(archivo_precios, 'rt') as file:
        data = csv.reader(file)
        precio_mercaderia = {}
        for line in data:
            try:
                precio_mercaderia[line[0]] = float(line[1])
            except IndexError:
                # Si encuentra una línea vacía, no quiero que haga nada.
                pass
    return precio_mercaderia


def balance_total(camion, precio_mercaderia):
    '''
    Función que devuelve el balance de operaciones, imprimiendo
    por pantalla lo que costó el camión, lo que se recaudó con la
    venta y la diferencia. Finalmente, informa si hubo ganancia o
    pérdida total en la operación.
    '''
    # Balance es la variable que guarda el valor neto de ganancia/pérdida
    balance = 0.0
    costo_total = 0.0
    precio_total = 0.0
    # Itero en cada elemento de la lista camión
    for producto in camion:
        # Busco si la fruta que se compró (en el camión) está en la lista
        # de frutas vendidas (precio_mercaderia).
        # En código, busco si existe esa key en el diccionario precio_mercaderia
        if producto['nombre'] in precio_mercaderia:
            # Acá se realizan los cálculos del costo, precio y balance
            precio = precio_mercaderia[producto['nombre']] * producto['cajones']
            costo = producto['cajones'] * producto['precio']
            
            costo_total += round(costo, 2)
            precio_total += round(precio, 2)
            balance += round(precio - costo, 2)
            # Y estas tres líneas fueron necesarias para comprobar que todo estaba bien.
            # print(f'Precio de {producto["nombre"]} = {precio_mercaderia[producto["nombre"]]:.2f} * {producto["cajones"]:.2f}')
            # print(f'Costo de {producto["nombre"]} = {producto["cajones"]:.2f} * {producto["precio"]:.2f}')
            # print(f'{producto["nombre"]} | {precio:.2f} | {costo:.2f} | {balance:.2f}')
    return balance, costo_total, precio_total


def main(archivo_camion, archivo_precios):
    '''
    Función principal del programa que llama a todas las demás.
    '''
    camion = leer_camion(archivo_camion)
    precio_mercaderia = leer_precios(archivo_precios)
    balance, costo, precio = balance_total(camion, precio_mercaderia)

    print(f'Balance de la situación')
    print(f'Costo del camión: ${costo:.2f} | Recaudación: ${precio:.2f} | Balance neto: ${balance:.2f}.')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2:
        archivo_camion = args[0]
        archivo_precios = args[1]

        # Confirmado el Nº de argumentos, largamos el programa.
        main(archivo_camion, archivo_precios)

    else:
        print('''Se ingresó un número inválido de argumentos:
            <2.15_balances.py> <../Data/camion.csv> <../Data/precios.csv>''')



#### OUTPUT ####
'''
Balance de la situación
Costo del camión: $47671.15 | Recaudación: $62986.10 | Balance neto: $15314.95.
'''
#### OUTPUT ####