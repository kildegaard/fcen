import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


N = 100000

# plt.plot(randomwalk(N))
# plt.show()

cant_caminatas = 12
fig = plt.figure(num=1, figsize=(10, 6), dpi=80, facecolor='grey', edgecolor='cyan', frameon=True)

caminatas = []
for _ in range(cant_caminatas):
    caminata = randomwalk(N)
    plt.subplot(2, 1, 1)
    plt.plot(caminata)

plt.show()
