import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=80)
plt.subplot(1, 1, 1)

colores = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

t = 2 * np.pi / 3
# plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
# plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.scatter(x=[0, 1, 2, 3], y=[1, 1, 4, 9], s=[10, 100, 1000, 10000], color=colores)

plt.show()

'''
Vamos a dejarlo asentado acá y en algún momento lo paso en limpio:

#? Con .plot puedo dibujar línas y con .scatter, puntitos

#* Se le pasan así las cosas cosas:
plt.plot(x=[x1, x2, ..., xn], y=[y1, y2, ..., yn], color = [puede ser vector], linewidth=1.5, linestyle='--')
plt.scatter(x=[0, 1, 2, 3], y=[1, 1, 4, 9], s=[10, 100, 1000, 10000], color=colores)

'''
