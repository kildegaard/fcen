# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:01:51 2020

@author: Y149681
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


plt.close('all')
df = pd.read_excel('Filtro_estacionario.xlsx')
H = df.to_numpy()
F = H[:, :2]
H = H[:, 2:]

VarFiltrar = 16
threshold = 15
[fila, col] = np.shape(H)

mx = np.zeros(fila)
mn = np.zeros(fila)

plt.figure()
plt.plot(F[:, 1], H[:, VarFiltrar])
plt.show()

w = 5
for i in range(np.int((w + 1) / 2), np.int(fila - (w - 1) / 2)):
    aux4 = H[np.int(i - (w - 1) / 2):np.int(i + (w - 1) / 2), VarFiltrar]
    mx[i] = np.max(aux4)
    mn[i] = np.min(aux4)

H = H[(mx - mn) < threshold, :]
F = F[(mx - mn) < threshold, :]

plt.scatter(F[:, 1], H[:, VarFiltrar], color='red')
plt.show()
