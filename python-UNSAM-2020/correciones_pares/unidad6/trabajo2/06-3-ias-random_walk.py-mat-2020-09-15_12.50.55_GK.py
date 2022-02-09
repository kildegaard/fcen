# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:08:56 2020

@author: USUARIO
"""
import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def busqueda_cercana(array, value):
    '''
    GK: Tuve que googlear un poco para ver qué hacían esos métodos. Te funciona, lo cual es genial, pero quizás
    lo que te faltó a mi entender es un poco de documentación al respecto, explicar qué hace o por qué lo hacés.
    '''
    return array.flat[np.abs(array - value).argmin()]


def maxomin(lista):
    '''
    GK: Acá estás tomando como parámetro "lista" pero dentro de la función lo usás como lista_promedios.
    Funciona igual, creo yo, porque lista_promedios es una variable GLOBAL (está definida fuera de las funciones), de
    modo que es posible ver su valor en cualquier scope.
    '''
    maximo = np.abs(max(lista_promedios))
    minimo = np.abs(min(lista_promedios))
    if (maximo > minimo):
        return max(lista_promedios)
    else:
        return min(lista_promedios)


N = 100000
cercano = 0
lista_caminatas = []
lista_promedios = []
plt.subplot(2, 1, 1)  # GK: Lo puse fuera del loop. No hace falta generar uno por cada caminata
for i in range(12):
    lista_caminatas.append(randomwalk(N))
    lista_promedios.append(sum(lista_caminatas[i]) / N)
    plt.plot(lista_caminatas[i])


maximo = maxomin(lista_promedios)

lista_promedios = np.array(lista_promedios)  # convierto a array
cercanoa0 = busqueda_cercana(lista_promedios, cercano)
lista_promedios = lista_promedios.tolist()
# print(cercanoa0)
# busqueda del mas cercano a cero
indice_min = lista_promedios.index(cercanoa0)
# print(indice_min)

# busqueda del mas lejano a cero
indice_max = lista_promedios.index(maximo)
# print(indice_max)


plt.xlabel('Tiempo')
plt.ylabel('Distancia al Origen')
plt.subplot(2, 2, 3)
plt.plot(lista_caminatas[indice_min], color='red')
plt.subplot(2, 2, 4)

plt.plot(lista_caminatas[indice_max], color='green')

plt.show()
