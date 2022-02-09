#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:51:39 2020

@author: mariano
"""

import random
from collections import Counter 

def truco_envido():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor, palo) for valor in valores for palo in palos]
    mano=random.sample(naipes,k=3)
    
    tenes_envido=Counter(p for v, p in mano)
    
    envido=0
    if len(set(tenes_envido))==2:
        palo_envido=tenes_envido.most_common()[0][0]
        valores_envido=[v for v, p in mano if p == palo_envido]
    
        for v in valores_envido:
            if v >= 10:
                envido+=10
            elif v <10:
                envido+=v+10
    return envido

resultados=[truco_envido() for i in range(1000000)]
probabilidad_31=(resultados.count(31)/len(resultados))
probabilidad_32=(resultados.count(32)/len(resultados))
probabilidad_33=(resultados.count(33)/len(resultados))
print('Probabilidades: ')
print('de sacar 31 de envido:', probabilidad_31)
print('de sacar 32 de envido:', probabilidad_32)
print('de sacar 33 de envido:', probabilidad_33)
      

