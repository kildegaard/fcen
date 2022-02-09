import random as rd
import os
from collections import Counter


def tirar_dados(dados):
    """
    Función que devuelve una lista de una tirada de n dados

    Args:
        dados (int): Cantidad de dados a tirar en una tirada

    Returns:
        list: Lista de dadoa en la tirada
    """
    tirada = [rd.randint(1, 6) for cant_dados in range(dados)]
    return tirada


def es_generala(tirada):
    """
    Función que dada una tirada de n dados te devuelve si es o no generala

    Args:
        tirada (list): Lista de tirada de n dados

    Returns:
        bool: es o no generala
    """
    # Verifico que todos los dados sean igual al primero (all devuelve True si todos sus valores lo son)
    esGen = all(tirada[0] == dado for dado in tirada) and len(tirada) == 5
    return esGen


def tiradas_totales(dados=5):
    """
    Función que lanza n dados hasta 3 veces y se verifica si se obtiene generala.
    Generala se da cuando los 5 valores son iguales entre sí.

    Args:
        dados (int, optional): Cantidad de dados. Defaults to 5.

    Returns:
        bool: es o no generala
    """
    # Empezamos suponiendo que no hay generala
    generala = False
    gen_servida = 0
    tiradas_max = 3
    cant_tiradas = 0
    lista_dados_tirados = []
    while not generala and cant_tiradas < tiradas_max:
        cant_tiradas += 1
        tirada = tirar_dados(dados)
        # voy a querer contar qué dados se repiten y cuántas veces lo hacen
        contar_dados = Counter(tirada)

        if cant_tiradas == 1:
            generala = es_generala(tirada)
            if generala:
                gen_servida = 1

        if not generala and cant_tiradas == 1:  # Es decir, para la primera tirada de dados...
            dado_mas_repe = contar_dados.most_common(1)[0][0]
            cant_repe = contar_dados.most_common(1)[0][1]
            # A ver, pasame la repe!
            lista_dados_tirados.extend([dado_mas_repe for repetido in range(cant_repe)])
            # Para la siguiente tirada vamos a tener menos dados
            dados -= cant_repe
        else:
            # Acá tendríamos la 2da y 3er tirada (si ocurren)
            lista_aux = [dado for dado in tirada if dado in lista_dados_tirados]
            lista_dados_tirados.extend(lista_aux)
            # Como la lista lista_aux solo puede llegar a tener valores de dado que ya estén en la lista
            # donde los vengo guardando (lista_dados_tirados) solo resta corroborar que sean 5 en total!
            if len(lista_dados_tirados) == 5:
                generala = True
            dados -= len(lista_aux)
        # cant_tiradas += 1
    # print(lista_dados_tirados)

    return generala, gen_servida


# resultado, _ = tiradas_totales()
# print(resultado)

cant_tiradas = 1000000

cant_generalas = 0
cant_generalas_servidas = 0
for ntirada, tirada in enumerate(range(cant_tiradas)):
    resultado, gen_servida = tiradas_totales()
    if resultado == True:
        cant_generalas += 1
        cant_generalas_servidas += gen_servida
    if ntirada % 10000 == 0:
        print(f'Vamos {(ntirada/cant_tiradas)*100:.2f}%', end='\r')


prob = float(cant_generalas / cant_tiradas) * 100
prob_servida = float(cant_generalas_servidas / cant_tiradas) * 100

print(f'En {cant_tiradas} tiradas salieron {cant_generalas} generalas ({cant_generalas_servidas} servidas).')
print(f'P(generala) = {prob:.4f}% -|- P(generala servida) = {prob_servida:.4f}%')
