import random
from busqueda_secuencial_modif import busqueda_secuencial_


def generar_lista(n, m):
    l = random.sample(range(m), k=n)
    l.sort()
    return l


def generar_elemento(m):
    return random.randint(0, m - 1)


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

comparaciones = experimento_secuencial_promedio(lista, m, k)
print(comparaciones)
