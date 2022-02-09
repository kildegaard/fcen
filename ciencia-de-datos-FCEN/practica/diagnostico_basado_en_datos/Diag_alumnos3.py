# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:01:58 2019

@author: Y149681
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
from sklearn.decomposition import PCA
import pandas as pd


plt.close('all')

df_H = pd.read_excel(open('train_alumnos.xls', 'rb'))


H = df_H.to_numpy()
(filas,col) = np.shape(H)
F = np.linspace(1,filas,filas)


# Fitro por distancia de Hotteling *********************
for a in range(4):
    print('Iteración nro: ',a)
    Hn = stats.zscore(H)
    S = np.linalg.pinv(np.cov(Hn.T))
    Hott = np.sum(Hn @ S * Hn,axis=1) 
    plt.figure()
    plt.scatter(F,Hott)
    plt.title('Filtro por Distancia de Mahalanobis')
    Queda = Hott<300
    H = H[Queda,:]
    F = F[Queda]
    Hott = Hott[Queda]
    plt.scatter(F,Hott)

    
    
    
    
    
Hn = stats.zscore(H)
S = np.linalg.pinv(np.cov(Hn.T))
Hott = np.sum(Hn @ S * Hn,axis=1) 
plt.figure()
plt.hist(Hott,bins=100)
plt.hist('Distribución de valores de distancia de Mahalanobis')
plt.figure()
plt.scatter(F,Hott)
plt.title('Datos Históricos: Distancia de Mahalanobis')
(filas,col) = np.shape(H)
LimHott = np.percentile(Hott, 99.999, axis=0)
plt.plot(LimHott*np.ones(filas),color = 'red')

alfa = np.linspace(0,0.999,1000)
percen_Hott = np.percentile(Hott, alfa*100, axis=0)
plt.figure()
plt.title('Función de probabilidad acumulada')
plt.plot(percen_Hott,alfa)
Lim_F = stats.f.ppf(alfa, dfn=col, dfd=filas-col) *col*(filas-1) / (filas-col)
plt.plot(Lim_F,alfa, color='red')
plt.legend(('P acumluada vs. percentil','P acumluada según Fisher'))
# MODELO PCA *************************************
Hz = stats.zscore(H)
pca=PCA()
pca.fit(Hz)
av=pca.explained_variance_ratio_

# Elijo nro de compoentes
expli=np.zeros(np.size(av))
expli[0]=av[0]
for a in range(1,np.size(av)):
    expli[a]=expli[a-1]+av[a]
    if expli[a]<.95:
        npc=a+1
# Contruyo modelo y residuo
Avm=np.asmatrix(pca.components_[0:npc,:])  
Avr=np.asmatrix(pca.components_[npc+1:,:])   

# Calculo los límites de los test
ConfT2a = 99.995 #%grado de confianza del test
ConfSPE = 99.995 #%grado de confianza del test 

T2aMAX = stats.f.ppf(ConfT2a/100, dfn=npc, dfd=filas-npc) *npc*(filas-1) / (filas-npc)
print(T2aMAX)

# Calculo T2a
Scorem = np.array(Hz @ Avm.T)
T2a = np.sum( Scorem * Scorem , axis=1)
T2aMAX = np.percentile(T2a, ConfT2a, axis=0)
plt.figure()
plt.plot(T2a)
plt.title('Serie temporal T2a para train')
plt.plot(T2aMAX*np.ones(np.shape(T2a)[0]))

# Calculo SSPE
Score = np.array(Hz @ Avr.T)
SScore = np.sum( Score * Score , axis=1)
mSPE = np.mean(SScore )
vSPE = np.var( SScore )

g1 = vSPE/(2**mSPE)
h1 = (2.*(mSPE**2))/vSPE

LimSPE = g1*stats.chi2.ppf(ConfSPE/100,h1)
LimSPE = np.percentile(SScore, ConfSPE, axis=0)

plt.figure()
plt.title('SSPE para training')
plt.plot(SScore)
plt.plot(LimSPE*np.ones(np.shape(T2a)[0]))

# ANALIZO DATOS TEST
df_H2 = pd.read_excel(open('test_alumnos.xls', 'rb'))
# Saco media y desvest con histórico de train
mH = np.mean(H,axis=0)
dH = np.std(H,axis=0)

H2 = df_H2.to_numpy()
(filas2,col2) = np.shape(H2)
F = np.linspace(1,filas2,filas2)
Hn2 = (H2-mH)/dH

Scorem = np.array(Hn2 @ Avm.T);
T2a = np.sum( Scorem**2 , axis=1)

plt.figure()
plt.title('T2a para test')
plt.plot(T2a)
plt.plot(T2aMAX*np.ones(np.shape(T2a)[0]))

# saco el spe
Score2 = np.array(Hn2 @ Avr.T);
SScore2 = np.sum( Score2**2 , axis=1)

# Los ploteo junto con el error
plt.figure()
plt.title('SSPE para test')
plt.plot(SScore2)
plt.plot(LimSPE*np.ones(np.shape(T2a)[0]))

# Saco el porte de cada variable al spe
TMEDZ = np.array(Hn2@Avm.T)

MEDZMOD = np.array(TMEDZ @ Avm)

MEDZERR = Hn2 - MEDZMOD

SPEDESC = MEDZERR**2

# Grafico el aporte frente a una falla
plt.figure()
plt.title('Aporte de cada variable al SSPE para la serie completa')
plt.pcolor(SPEDESC)
plt.figure()
plt.title('Aporte de cada variable al SSPE para un dato típico')
plt.bar(range(col2),SPEDESC[158,:])

plt.figure()
plt.title('Relación entre las variables identificadas')
plt.scatter(Hn[:,23],Hn[:,35], label="train")
plt.plot(Hn2[:,23],Hn2[:,35], label="test",color='red')


# plt.figure()
# plt.plot(H[:,47])
# plt.plot(H2[:,47])