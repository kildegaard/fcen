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


def calculo_costo_camion(camion):
    '''
    Función que calcula el valor de coste de cada fruta
    teniendo en cuenta cantidad de cajones y su precio.
    Estos datos los guarda en una lista de tuplas.
    Adicionalmente, se calcula el valor total del camión
    y se devuelve como un float.
    '''
    costo_frutas = []
    costo_total = 0.0
    for frutas in camion:
        valor = round(frutas['cajones'] * frutas['precio'], 2)
        costo_total += valor
        costo_frutas.append((frutas['nombre'], valor))
    return costo_frutas, costo_total


def leer_precios(archivo_precios):
    '''
    Esta función levanta un .csv con información del precio
    de venta de los cajones de fruta y verdura
    vendidos y devuelve un diccionario con dicha información.
    Adicionalmente, devuelve el valor total recaudado como float.
    '''
    with open(archivo_precios, 'rt') as file:
        data = csv.reader(file)
        precio_mercaderia = {}
        precio_total = 0.0
        for line in data:
            try:
                precio_mercaderia[line[0]] = float(line[1])
                precio_total += float(line[1])
            except IndexError:
                # Si encuentra una línea vacía, no quiero que haga nada.
                pass
    return precio_mercaderia, precio_total


def balance(costo_frutas, precio_mercaderia, costo_total, precio_total):
    print('''
    Balance de compra / venta de mercadería
    =======================================
    ''')

    print(f'Compra de mercadería\n')
    print(f'Frutas \t\t Valor')
    for frutas in costo_frutas:
        print(f' {frutas[0]:<12s} \t ${frutas[1]:>10.2f}.-')
    print(f'Costo total: ${costo_total:.2f}.-\n')

    print(f'Venta de mercadería\n')
    print(f'Mercadería \t Valor')
    for mercaderia in precio_mercaderia:
        print(
            f' {mercaderia:<12s} \t ${precio_mercaderia[mercaderia]:>10.2f}.-')
    print(f'Ingreso total: ${costo_total:.2f}.-\n')

    print(f'Balance: ${precio_total-costo_total:.2f}.-')


def main(archivo_camion, archivo_precios):
    '''
    Función principal del programa que llama a todas las demás.
    '''
    camion = leer_camion(archivo_camion)
    costo_frutas, costo_total = calculo_costo_camion(camion)
    precio_mercaderia, precio_total = leer_precios(archivo_precios)
    # print(f'El costo de la fruta {costo_frutas[0][0]} es de ${costo_frutas[0][1]:.2f}.-')

    balance(costo_frutas, precio_mercaderia, costo_total, precio_total)


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
