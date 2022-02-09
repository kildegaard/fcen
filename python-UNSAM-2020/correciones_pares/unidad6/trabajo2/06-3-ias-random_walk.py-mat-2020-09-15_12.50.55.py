# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:08:56 2020

@author: USUARIO
"""
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def busqueda_cercana(array,value):
       return array.flat[np.abs(array - value).argmin()]

def maxomin(lista):
    maximo=np.abs(max(lista_promedios))
    minimo=np.abs(min(lista_promedios)) 
    if (maximo>minimo):
        return max(lista_promedios)
    else: return min(lista_promedios)


N = 100000
cercano=0
lista_caminatas=[]
lista_promedios=[]
for i in range(12):
    lista_caminatas.append(randomwalk(N))
    lista_promedios.append(sum(lista_caminatas[i])/N)
    plt.subplot(2, 1, 1) # define la figura de arriba
    plt.plot(lista_caminatas[i])


maximo = maxomin(lista_promedios)

lista_promedios = np.array(lista_promedios) #convierto a array
cercanoa0 =busqueda_cercana(lista_promedios,cercano)
lista_promedios = lista_promedios.tolist()
#print(cercanoa0)
#busqueda del mas cercano a cero
indice_min = lista_promedios.index(cercanoa0)
#print(indice_min)

#busqueda del mas lejano a cero
indice_max = lista_promedios.index(maximo)
#print(indice_max)



plt.xlabel('Tiempo')
plt.ylabel('Distancia al Origen')
plt.subplot(2,2,3)
plt.plot(lista_caminatas[indice_min], color='red')
plt.subplot(2,2,4)

plt.plot(lista_caminatas[indice_max], color='green')

plt.show()
