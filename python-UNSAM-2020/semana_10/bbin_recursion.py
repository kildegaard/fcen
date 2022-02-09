# -*- coding: utf-8 -*-
# Ejercicio 10.11 - Búsqueda binaria con recursión


def bbin(lista, e):
    inicio = 0
    fin = len(lista) - 1
    res = True

    def bbin_aux(lista, e, inicio, fin):
        if inicio > fin:
            return False

        medio = (inicio + fin) // 2
        if e == lista[medio]:
            return True
        if e < lista[medio]:
            return bbin_aux(lista, e, inicio, medio - 1)
        return bbin_aux(lista, e, medio + 1, fin)
    res = bbin_aux(lista, e, inicio, fin)
    return res

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
