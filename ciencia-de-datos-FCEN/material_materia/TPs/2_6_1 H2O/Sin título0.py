# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:34:14 2020

@author: Y149681
"""

import numpy as np
from matplotlib import pyplot as plt

H = np.random.normal(loc=0.0, scale=1.0, size=(13,4))
H[:,1] = H[:,0]+

C = np.cov(H.T)

D = np.linalg.det(C)
"""
plt.figure()
plt.imshow(C)
plt.colorbar()

pos = H > 0
repeti = np.sum(pos,axis=0)

plt.figure()
plt.hist(repeti, bins=8)

Cr = np.zeros((100,100))

for i in range(99):
    for j in range(i+1,100):
        for fila in range(10):
            if H[fila,i] * H[fila,j] <0:
                #print( 'i=', i,'  j=', j,'  fila=',fila,' p1=',H )
                Cr[i,j] = Cr[i,j] + 1
                
Cr2 = np.ravel(Cr)
Cr2 = Cr2[Cr2>0]

plt.figure()
plt.hist(Cr2)
"""