# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:57:02 2020

@author: Ayelen
"""
import sys
import csv

# def parse_csv(nombre_archivo):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)

#         # Lee los encabezados
#         headers = next(rows)
#         registros = []
#         for row in rows:
#             if not row:    # Saltea filas sin datos
#                 continue
#             registro = dict(zip(headers, row))
#             registros.append(registro)

#     return registros


#import csv
# tuve que poner types str, float, float para que me pueda convertir tanto los precios de 'precios.csv' como los de 'camion.csv' si pongo int, esto no es posible
def parse_csv(nombre_archivo, select=None, types=[str, float, float], has_headers=False):  # Com: no hace falta poner tipos x default, es algo que le pasás por comandos
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
       # registros = []
       # registro = {}

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]  # Com: buenos nombres de variables!
                encabezados = select
            else:
                indices = []

            registros = []
            #registro = {}
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

                registro = dict(zip(encabezados, fila))
                # print(registro)
                registros.append(registro)

        else:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]  # falta separar en tuplas si no hay headers, entonces no hago encabezado
                    # print(fila)
            # Armar tupla                #registro = dict()
                registro = tuple()

                registro = tuple(fila)
                # print(registro)
                registros.append(registro)

    return registros

#b = sys.modules


# a = parse_csv('Data/precios.csv', has_headers=False)


# if types:
#   fila = [func(val) for func, val in zip(types, fila) ]
