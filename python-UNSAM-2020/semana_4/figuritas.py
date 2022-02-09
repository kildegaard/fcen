# Ejercicio sobre el album de figuritas del Mundial

import numpy as np
import random as rd
from pprint import pprint as pp
import matplotlib.pyplot as plt

### PARÁMETROS DEL PROGRAMA ###

cant_figus_total = 670
n_repeticiones = 1000

### ----------------------- ###


def crear_album(figus_total):
    """
    Función que crea un album de figus.
    Se genera un arreglo con ceros por cada posición de figurita representando
    el hecho que no está pegada en el mismo.
    Args:
        figus_total (int): Cantidad total de figuritas en el album

    Returns:
        ndarray: lista de ceros por cada figu en el album
    """
    album_vacio = np.zeros(figus_total, dtype=int)
    # album_vacio = np.ones(figus_total)
    return album_vacio


def album_incompleto(album):
    """
    Función que devuelve True si el album aún no está completo
    Args:
        album (ndarray): lista de valores que representa el album

    Returns:
        bool: está o no completo
    """
    # Alternativa más corta
    # incompleto = any((album == 0))
    incompleto = False
    for figu in album:
        if figu == 0:
            incompleto = True
    return incompleto


def album_solidario_incompleto(album, cant_amigos=5):
    incompleto = False
    for figu in album:
        if figu < cant_amigos:
            incompleto = True
    return incompleto


def comprar_figu(figus_total):
    """
    Función que devuelve una figu al azar
    Args:
        figus_total (int): Cantidad de figus totales
    """
    figu = rd.randint(0, figus_total-1)
    return figu


def cuantas_figus(figus_total):
    """
    Función que crea album, compra figus hasta que se completa y devuelve dicho valor.
    Adicionalmente, devuelve el album (para chusmear qué pasó)
    Args:
        figus_total (ndarray): Total de figuritas del album

    Returns:
        int, ndarrat: Devuelve el total de figus compradas y el album en sí
    """
    album = crear_album(figus_total)
    cant_figus_compradas = 0
    while album_incompleto(album):
        figu_comprada = comprar_figu(figus_total)
        album[figu_comprada] += 1
        cant_figus_compradas += 1
    return cant_figus_compradas, album


def comprar_paquete(figus_total, figus_paquete):
    paquete = np.array([rd.randint(0, figus_total-1) for figu in range(figus_paquete)])
    return paquete


def comprar_paquete_sin_repe(figus_total, figus_paquete):
    posibilidades = [valor for valor in range(0, 670)]
    paquete = rd.sample(posibilidades, k=5)
    return paquete


def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cant_paquetes_comprados = 0
    while album_incompleto(album):
        paquete_comprado = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete_comprado:
            album[figu] += 1
        cant_paquetes_comprados += 1
    return cant_paquetes_comprados


def cuantos_paquetes_solidarios(figus_total, figus_paquete, cant_amigos):
    album = crear_album(figus_total)
    cant_paquetes_comprados = 0
    while album_solidario_incompleto(album, cant_amigos):
        paquete_comprado = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete_comprado:
            album[figu] += 1
        cant_paquetes_comprados += 1
    return cant_paquetes_comprados


def cuantos_paquetes_sin_repe(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cant_paquetes_comprados = 0
    while album_incompleto(album):
        paquete_comprado = comprar_paquete_sin_repe(figus_total, figus_paquete)
        for figu in paquete_comprado:
            album[figu] += 1
        cant_paquetes_comprados += 1
    return cant_paquetes_comprados

##### EJECUCIÓN DEL PROGRAMA #####


# Ejercicio 4.18
'''
cant_figu, album = cuantas_figus(cant_figus_total)
print(cant_figu)
pp(album)
'''
##################################

# Ejercicio 4.19
'''
# Parámetros iniciales del programa
n_repeticiones = 1000
figus_total = 6

lista_figus = np.array([cuantas_figus(figus_total)[0] for repe in range(n_repeticiones)])
promedio_figus = round(np.average(lista_figus), 0)
print(lista_figus[:10])
print(f'Se necesitan comprar, en promedio, {promedio_figus:.0f} figuritas para llenar un album de {figus_total} figus.')

# Output:
# [15  6 19 16  8 25 11 24 11 25]
# Se necesitan comprar, en promedio, 15 figuritas para llenar un album de 6 figus.
'''
##################################

# Ejercicio 4.20
'''
# Parámetros iniciales del programa
n_repeticiones = 100
figus_total = 670

lista_figus = np.array([cuantas_figus(figus_total)[0] for repe in range(n_repeticiones)])
promedio_figus = round(np.average(lista_figus), 0)
print(lista_figus[:10])
print(f'Se necesitan comprar, en promedio, {promedio_figus:.0f} figuritas para llenar un album de {figus_total} figus.')

# Output:
# [4651 5597 3571 3919 5062 3455 3549 3888 4865 4845]
# Se necesitan comprar, en promedio, 4640 figuritas para llenar un album de 670 figus.
'''
##################################

# Ejercicio 4.21
'''
# Parámetros iniciales del programa
figus_total = 670
figus_paquete = 5

paquete = comprar_paquete(figus_total, figus_paquete)
print(paquete)

# Output:
# [106 663 206 360 160]
'''
#################################

# Ejercicio 4.23
'''
# Parámetros iniciales del programa
figus_total = 670
figus_paquete = 5

cant_paquetes = cuantos_paquetes(figus_total, figus_paquete)
print(f'Se necesitaron comprar {cant_paquetes:.0f} paquetes para llenar un album de {figus_total} figus.')
print(f'Osea, un total de {cant_paquetes*5:.0f} figuritas.')

# Output:
# Se necesitaron comprar 774 paquetes para llenar un album de 670 figus.
# Osea, un total de 3870 figuritas.
'''
################################

# Ejercicio 4.24
'''
# Parámetros iniciales del programa
figus_total = 670
figus_paquete = 5
n_repeticiones = 100

lista_figus = np.array([cuantos_paquetes(figus_total, figus_paquete) for repe in range(n_repeticiones)])
promedio_paquetes = round(np.mean(lista_figus), 0)

print(f'Se necesitan comprar, en promedio, {promedio_paquetes:.0f} paquetes para llenar un album de {figus_total} figus.')
print(f'Osea, un total de {promedio_paquetes*5:.0f} figuritas.')

# Output:
# Se necesitan comprar, en promedio, 949 paquetes para llenar un album de 670 figus.
# Osea, un total de 4745 figuritas.
'''
#################################

# Ejercicio 4.25
'''
# Parámetros iniciales del programa
figus_total = 670
figus_paquete = 5
n_repeticiones = 500
num_paquetes_comprados = 850

universo_de_posibilidades = np.array([cuantos_paquetes(figus_total, figus_paquete) for repe in range(n_repeticiones)])
menos_de_850 = [album for album in universo_de_posibilidades if album <= num_paquetes_comprados]

probabilidad = (len(menos_de_850) / len(universo_de_posibilidades)) * 100
print(f'La probabilidad de completar un album de {figus_total} figuritas comprando {num_paquetes_comprados} paquetes o menos es del {probabilidad}%.')

# Output:
# La probabilidad de completar un album de 670 figuritas comprando 850 paquetes o menos es del 30.0%.
'''
################################

# Ejercicio 4.26
'''
# Esto es del 4.20
# Parámetros iniciales del programa
n_repeticiones = 100
figus_total = 670

lista_figus_20 = np.array([cuantas_figus(figus_total)[0] for repe in range(n_repeticiones)])
plt.hist(lista_figus_20, bins=50, density=True, color='b')
# plt.show()


# Esto es del 4.24
# Parámetros iniciales del programa
n_repeticiones = 100
figus_total = 670
figus_paquete = 5

lista_figus_24 = np.array([cuantos_paquetes(figus_total, figus_paquete)*5 for repe in range(n_repeticiones)])
plt.hist(lista_figus_24, bins=50, density=True, color='g')
plt.show()
'''
################################

# Ejercicio 4.27
'''
# Parámetros iniciales del programa
n_repeticiones = 100
figus_total = 670
figus_paquete = 5
probabilidad = 0.9

total_posibilidades = np.array([cuantos_paquetes(figus_total, figus_paquete) for repe in range(n_repeticiones)])

paquetes_a_comprar_estimados = probabilidad * total_posibilidades.mean()

print(f'La cantidad de paquetes(estimados) a comprar para tener un 90 % de chances de completar el album es de {paquetes_a_comprar_estimados:.0f}.')

# Output:
La cantidad de paquetes(estimados) a comprar para tener un 90 % de chances de completar el album es de 854.
'''
################################

# Ejercicio 4.28
'''
# Parámetros iniciales del programa
figus_total = 670
figus_paquete = 5
n_repeticiones = 100

lista_figus = np.array([cuantos_paquetes_sin_repe(figus_total, figus_paquete) for repe in range(n_repeticiones)])
promedio_paquetes = round(np.mean(lista_figus), 0)

print(f'Se necesitan comprar, en promedio, {promedio_paquetes:.0f} paquetes (sin repes) para llenar un album de {figus_total} figus.')
print(f'Osea, un total de {promedio_paquetes*5:.0f} figuritas.')

# Output:
# Se necesitan comprar, en promedio, 918 paquetes (sin repes) para llenar un album de 670 figus.
# Osea, un total de 4590 figuritas.
'''
################################

# Ejercicio 4.29

# Parámetros iniciales del programa
figus_total = 670
figus_paquete = 5
cant_amigos = 5
n_repeticiones = 100

lista_figus = np.array([cuantos_paquetes_solidarios(figus_total, figus_paquete, cant_amigos) for repe in range(n_repeticiones)])
promedio_paquetes = round(np.mean(lista_figus), 0)

print(f'Para completar {cant_amigos} álbumes de {figus_total} figuritas, se necesitan comprar, en promedio, unos {promedio_paquetes:.0f} paquetes.')
