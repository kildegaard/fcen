# Ejercicio 4.6 - Generala servida

import random as rd


def tirar_dados(dados, tiradas):
    """
    Función que devuelve lista de listas de tiradas de n dados

    Args:
        dados (int): Cantidad de dados a tirar en una tirada
        tiradas (int): Cantidad de tiradas a realizar

    Returns:
        list: Lista de listas de tiradas
    """
    lista = [[rd.randint(1, 6) for cant_dados in range(dados)] for cant_tiradas in range(tiradas)]
    return lista


def es_generala(tirada):
    """
    Función que dada una tirada de n dados te devuelve si es o no generala

    Args:
        tirada (list): Lista de tirada de n dados

    Returns:
        bool: es o no generala
    """
    # Verifico que todos los dados sean igual al primero (all devuelve True si todos sus valores lo son)
    esGen = all(tirada[0] == dado for dado in tirada)
    return esGen


cant_dados = 5
cant_tiradas = 100000

pool = tirar_dados(cant_dados, cant_tiradas)
cant_generalas = 0
for tirada in pool:
    if es_generala(tirada):
        cant_generalas += 1

prob = float(cant_generalas / cant_tiradas) * 100

print(f'En {cant_tiradas} tiradas salieron {cant_generalas} generalas. P(generala) = {prob:.4f}%')

prob_exacta = 1 * (1/6) ** 4 * 100
print(f'La probabilidad exacta que ocurra una generala es de {prob_exacta:.4f}%')

dif = abs(prob - prob_exacta) / prob_exacta

print(f'El error relativo cometido por la estimación es {dif:.4f}%')
