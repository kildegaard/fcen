# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 23:09:06 2020

@author: mcarl
"""
import random

# Com: Yo hubiera puesto primero las definiciones y luego la parte de scripting
# envido.py
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor, palo) for valor in valores for palo in palos]
random.sample(naipes, k=3)  # Com: linea no necesaria


def envido_31(lista):
    mano = random.sample(lista, k=3)
    tanto = False
    excluidos = [10, 1]
    if mano[0][1] == mano[1][1] and mano[0][0] + mano[1][0] == 11 and mano[0][0] not in excluidos:
        tanto = True
    if mano[0][1] == mano[2][1] and mano[0][0] + mano[2][0] == 11 and mano[2][0] not in excluidos:
        tanto = True
    if mano[1][1] == mano[2][1] and mano[1][0] + mano[2][0] == 11 and mano[1][0] not in excluidos:
        tanto = True
    return tanto


def envido_32(lista):
    mano = random.sample(lista, k=3)
    tanto = False
    excluidos = [1, 2, 10, 11]
    if mano[0][1] == mano[1][1] and mano[0][0] + mano[1][0] == 11 and mano[0][0] not in excluidos:
        tanto = True
    if mano[0][1] == mano[2][1] and mano[0][0] + mano[2][0] == 11 and mano[2][0] not in excluidos:
        tanto = True
    if mano[1][1] == mano[2][1] and mano[1][0] + mano[2][0] == 11 and mano[1][0] not in excluidos:
        tanto = True
    return tanto


def envido_33(lista):
    mano = random.sample(lista, k=3)
    tanto = False
    excluidos = [1, 2, 3, 10, 11]  # Com: interesante forma de evaluar los envidos!
    if mano[0][1] == mano[1][1] and mano[0][0] + mano[1][0] == 11 and mano[0][0] not in excluidos:
        tanto = True
    if mano[0][1] == mano[2][1] and mano[0][0] + mano[2][0] == 11 and mano[2][0] not in excluidos:
        tanto = True
    if mano[1][1] == mano[2][1] and mano[1][0] + mano[2][0] == 11 and mano[1][0] not in excluidos:
        tanto = True
    return tanto


# print(envido_31(naipes))
N = 1000000
G = sum([envido_31(naipes) for i in range(N)])  # Com: bien usadas las list comprehension
prob = G / N  # Com: nombre de variables poco descriptivas
print(f'Tiré {N} veces, de las cuales {G} saqué 31 de envido.')
print(f'Podemos estimar la probabilidad de sacar 31 de envido mediante la formula G/N = {prob:.6f}.')

G = sum([envido_32(naipes) for i in range(N)])
prob = G / N
print(f'Tiré {N} veces, de las cuales {G} saqué 32 de envido.')
print(f'Podemos estimar la probabilidad de sacar 32 de envido mediante la formula G/N = {prob:.6f}.')

G = sum([envido_33(naipes) for i in range(N)])
prob = G / N
print(f'Tiré {N} veces, de las cuales {G} saqué 33 de envido.')
print(f'Podemos estimar la probabilidad de sacar 33 de envido mediante la formula G/N = {prob:.6f}.')
# Com: La parte de las probabilidades se podría haber hecho todo de una
