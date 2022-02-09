# -*- coding: utf-8 -*-

# Ejercicio 9.2 - Iteración sobre objetos

class Camion:
    """Clase camion"""

    def __init__(self, lotes):
        """Constructor"""

        self._lotes = lotes


    def precio_total(self):
        """Devuelve el precio total del camion"""

        res = sum([l.costo() for l in self._lotes])
        return res


    def contar_cajones(self):
        """Cuenta la cantidad de cajones"""

        from collections import Counter
        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

    def __iter__(self):
        """iterador"""

        return self._lotes.__iter__()

    def mostrar(self):
        res  = 'Lotes: <'
        for elem in self._lotes:
            res += f' | {elem} | '
        res += '>'
        print(res)


    def __len__(self):
        return len(self._lotes)

    def __getitem__(self, index):
        return self._lotes[index]

    def __contains__(self, nombre):
        res = any( [ lote.nombre == nombre for lote in self._lotes ] )
        return res
