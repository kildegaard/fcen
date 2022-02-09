# -*- coding: utf-8 -*-
# Ejercicio 11.4 - Experimentando con los 3 métodos de ordenamiento

def generar_lista(N):
    """Genera una lista de largo N con valores aleatorios entre 1 y 1000"""
    import random
    lista = []

    for i in range(N):
        lista.append(random.randint(1, 1000))
    return lista


