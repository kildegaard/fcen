import matplotlib.pyplot as plt
import numpy as np
import random
from busqueda_secuencial_modif import busqueda_secuencial_
from busqueda_binaria_con_contador import busqueda_binaria


def generar_elemento(m):
    return random.randint(0, m - 1)


def generar_lista(n, m):
    l = random.sample(range(m), k=n)
    l.sort()
    return l


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


m = 10000
k = 1000

comparaciones = 256

largos = np.arange(comparaciones) + 1  # estos son los largos de listas que voy a usar
comps_promedio_sec = np.zeros(comparaciones)  # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y comparaciones.

comps_promedio_bin = np.zeros(comparaciones)

for i, n in enumerate(largos):
    lista = generar_lista(n, m)  # genero lista de largo n
    comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos, comps_promedio_sec, label='Búsqueda Secuencial', marker='.')
plt.plot(largos, comps_promedio_bin, label='Búsqueda Binaria', linestyle='--')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()
