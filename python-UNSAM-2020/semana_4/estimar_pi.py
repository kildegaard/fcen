# Ejercicio 4.10 - Estimar pi

import random as rd


def generar_punto():
    x = rd.random()
    y = rd.random()
    return (x, y)


def dentro_circulo(punto):
    esta_adentro = False
    x, y = punto
    if x**2 + y**2 < 1:
        esta_adentro = True
    return esta_adentro


n_puntos = 100000
puntos_dentro = 0
puntos_fuera = 0
for _ in range(n_puntos):
    punto = generar_punto()
    if dentro_circulo(punto):
        puntos_dentro += 1
    else:
        puntos_fuera += 1

estimación_pi = round(4 * puntos_dentro / n_puntos, 5)

print(f'El valor de pi es, aproximadamente, {estimación_pi} ({n_puntos} iteraciones).')
