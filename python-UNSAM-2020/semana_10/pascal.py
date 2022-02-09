# -*- coding: utf-8 -*-

# Ejercicio 10.9 - Triángulo de Pascal

def pascal(fil, col):
    """
    Función que devuelve el valor (fil, col) dentro de un
    triángulo de Pascal
    """
    # Condiciones de contorno
    if fil == 0 or col == 0:
        return 1
    if fil == col:
        return 1

    res = pascal(fil - 1, col - 1) + pascal(fil - 1, col)
    return res
