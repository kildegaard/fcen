# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:01:13 2020

@author: Alfredo Farjat (afarjat@gmail.com)
"""


# %% Ejercicio 6.10

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


# Parametros
p = 11  # numero de caminatas
N = 100000  # numero de pasos

# Inicializo RW matriz
RW = np.zeros((p, N))
for i in range(p):
    RW[i, ] = randomwalk(N)

# Maximas desviacions
max_devs = np.zeros(p)
for i in range(p):
    max_devs[i] = max(abs(RW[i, ]))

max_index = np.argmax(max_devs)

# Minimas desviaciones
min_devs = np.zeros(p)
for i in range(p):
    min_devs[i] = min(abs(RW[i, ]))

min_index = np.argmin(min_devs)

# Colores
colores = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow'] * 2


# Hacer el plot
fig = plt.figure(figsize=(10, 6), dpi=80)
plt.subplot(2, 1, 1)  # define la figura de arriba
for i in range(p):
    plt.plot(RW[i, ], color=colores[i])
plt.xlim(0, N)
plt.ylim(-1000, 1000)
plt.xticks([])
plt.title('12 caminatas al azar')

plt.subplot(2, 2, 3)  # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot(RW[max_index, ], color='red')
plt.ylim(-1000, 1000)
plt.xticks([])
plt.title('Mayor desviacion')

plt.subplot(2, 2, 4)  # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot(RW[min_index, ], color='blue')
plt.ylim(-1000, 1000)
plt.xticks([])
plt.title('Menor desviacion')

plt.show()
