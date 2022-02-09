# -*- coding: utf-8 -*-

# Ejercicio 4.8 - Envido
import random as rd
import sys
from pprint import pprint as pp
from collections import Counter
from progress.bar import ChargingBar


def generar_mazo():
    """
    Función que genera un mazo de cartas española.
    Devuelve lista de diccionarios.

    Returns:
        list: Mazo de 10 cartas con 4 palos y sus valores para el envido
    """
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['basto', 'oro', 'espada', 'copa']
    mazo = [{'valor': valor, 'palo': palo} for valor in valores for palo in palos]
    # Acá agrego detalle del valor real de las cartas a la hora de contabilizar el envido
    for carta in mazo:
        if carta['valor'] in [10, 11, 12]:
            carta['valor envido'] = 0
        else:
            carta['valor envido'] = carta['valor']

    # mazo = [(valor, palo) for valor in valores for palo in palos]

    return mazo


def sacar_cartas(mazo):
    """
    Función que recibe un mazo y devuelve 3 cartas al azar sin reposición.

    Args:
        mazo (list): Mazo de cartas españolas

    Returns:
        list: Lista de 3 cartas extraídas al azar
    """
    mano = rd.sample(mazo, k=3)
    return mano


def calcula_envido(mano):
    valor_envido = 0
    carta_1 = mano[0]
    carta_2 = mano[1]
    carta_3 = mano[2]
    if carta_1['palo'] == carta_2['palo'] == carta_3['palo']:
        valor_envido = 20 + sum(sorted([carta['valor envido'] for carta in mano], reverse=True)[:2])
    elif carta_1['palo'] == carta_2['palo']:
        valor_envido = 20 + carta_1['valor envido'] + carta_2['valor envido']
    elif carta_1['palo'] == carta_3['palo']:
        valor_envido = 20 + carta_1['valor envido'] + carta_3['valor envido']
    elif carta_2['palo'] == carta_3['palo']:
        valor_envido = 20 + carta_2['valor envido'] + carta_3['valor envido']
    else:
        valor_envido = max([carta['valor envido'] for carta in mano])
    return valor_envido


def mensaje(mano, envido):
    print(f'Se obtuvieron las siguientes cartas:')
    print(f'>{mano[0]["valor"]} de {mano[0]["palo"]}')
    print(f'>{mano[1]["valor"]} de {mano[1]["palo"]}')
    print(f'>{mano[2]["valor"]} de {mano[2]["palo"]}')
    print(f'Valor del envido: {envido}')


def calculo_probabilidad(cant_repe):
    contabilidad_envido = Counter()
    jugadas = [jugar_mano() for repes in range(cant_repe)]
    barra_progreso = ChargingBar('Calculando jugadas..:', max=cant_repe)
    for envido in jugadas:
        barra_progreso.next()
        contabilidad_envido[envido] += 1
    barra_progreso.finish()

    envidos = list(sorted(contabilidad_envido.items()))
    probabilidades = [round((envidos[1] / cant_repe) * 100, 4) for envidos in sorted(contabilidad_envido.items())]

    print('Cálculo de la probabilidad de envidos')
    print(f'Cantidad total de manos: {cant_repe}.')
    for envido, prob in zip(envidos, probabilidades):
        print(f'Hubo {envido[1]:>6d} envido/s de {envido[0]:>3d} - Probabilidad {prob:>6.2f}%')


def jugar_mano(debug=False):
    mazo = generar_mazo()
    cartas_extraidas = sacar_cartas(mazo)
    valor_envido = calcula_envido(cartas_extraidas)
    if debug:
        mensaje(mano=cartas_extraidas, envido=valor_envido)
    return valor_envido


def main(argumentos):
    # jugar_mano()
    if len(argumentos) == 0:
        repeticiones = 10000
        print(f'No se aclaró cantidad de repeticiones. Default = {repeticiones:,d}')
    else:
        repeticiones = int(argumentos[0])

    calculo_probabilidad(repeticiones)


if __name__ == '__main__':
    main(sys.argv[1:])
