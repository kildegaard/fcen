# Árboles versión semana 4 - con gráficos!

import os
import matplotlib.pyplot as plt
import csv
import sys
from collections import Counter
from pprint import pprint
import numpy as np


def leer_parque(nombre_archivo, parque):
    '''
    Función que abre el archivo indicado y devuelve una lista de diccionarios
    con la información del parque especificado.
    '''
    with open(nombre_archivo, 'rt', encoding='utf8') as file:
        filas = csv.reader(file)
        headers = next(filas)
        lista_arboles = []
        for fila in filas:
            data = dict(zip(headers, fila))
            try:
                if data['espacio_ve'] == parque:
                    # Casteo las variables para que sean del tipo adecuado
                    data['altura_tot'] = int(data['altura_tot'])
                    data['diametro'] = int(data['diametro'])
                    data['inclinacio'] = int(data['inclinacio'])
                    # Armo la lista en sí
                    lista_arboles.append(data)
            except:
                print('Ocurrió algún problema.')
    return lista_arboles


def leer_arboles(nombre_archivo):
    """
    Función que recibe un archivo .csv y devuelve una lista con todos los árboles encontrados (en diccionarios)

    Args:
        nombre_archivo (string): archivo .csv de entrada de datos

    Returns:
        list: lista de diccionario
    """
    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        filas = csv.reader(file)
        headers = next(filas)
        lista_de_arboles = [{key: value for key, value in zip(headers, fila)} for fila in filas]
    return lista_de_arboles


def especies(lista_arboles):
    '''
    Función que toma una lista de árboles como la generada en leer_parque y
    devuelve el conjunto de especies.
    '''
    conj_especies = set()
    for arboles in lista_arboles:
        conj_especies.add(arboles['nombre_com'])

    return conj_especies


def contar_ejemplares(lista_arboles):
    '''
    Función que, dada una lista de árboles, devuelve un diccionario en el que
    las especies son las claves y tienen como valores asociados la cantidad
    de ejemplares en dicha especie.
    '''
    cant_ejemplares = Counter()
    for arbol in lista_arboles:
        cant_ejemplares[arbol['nombre_com']] += 1

    # Había puesto esta línea porque piden devolver un diccionario, no una instancia de Counter
    # return dict(cant_ejemplares)
    return cant_ejemplares


def obtener_alturas(lista_arboles, especie):
    '''
    Función que dada una lista de árboles y una especie en particular devuelve
    una lista con las alturas de los ejemplares.

    Para llamra esta función por línea de comandos:
    python probando.py '<path al .csv>' '<parque>' '<especie>'
    '''
    lista_alturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_alturas.append(arbol['altura_tot'])

    return lista_alturas


def obtener_inclinaciones(lista_arboles, especie):
    """
    Función que, dada una lista de árboles y una especie en particular, devuelve una
    lista con las alturas de los ejemplares de esa especie.

    Args:
        lista_arboles (list): lista de diccionarios con los datos de todos los árboles del parque
        especie (string): nombre de la especie (dato en 'altura_tot' del .csv original)
    """
    lista_inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion = arbol['inclinacio']
            lista_inclinaciones.append(inclinacion)

    return lista_inclinaciones


def especimen_mas_inclinado(lista_arboles):
    '''
    Función que, dada una lista de árboles, devuelva la especie que tiene el
    ejemplar más inclinado y su inclinación.
    '''
    mi_set = especies(lista_arboles)
    lista_especies_max_incl = []
    for arbol in mi_set:
        # Guardo el máximo valor de la lista que regresa obtener_inclinaciones
        inclinac_arbol_max = max(obtener_inclinaciones(lista_arboles, arbol))
        # Guardo (altura máx, especie-arbol) del espécimen más alto para dicha especie
        lista_especies_max_incl.append((inclinac_arbol_max, arbol))

    # Me devuelve el primer elemento (de mayor a menor) que es una tupla
    return sorted(lista_especies_max_incl, reverse=True)[0]


def especie_promedio_mas_inclinada(lista_arboles):
    '''
    Función que, dada una lista de árboles, devuelve la especie que, en promedio,
    tiene la mayor inclinación. También devuelve el promedio calculado.
    '''
    mi_set = especies(lista_arboles)

    lista_inclinaciones_arboles = []
    for arbol in mi_set:
        suma = sum(obtener_inclinaciones(lista_arboles, arbol))
        cant_arboles = contar_ejemplares(lista_arboles)[arbol]
        inclin_prom = float(suma / cant_arboles)
        lista_inclinaciones_arboles.append((inclin_prom, arbol))
        # print(f'Árbol: {arbol} -|- Suma: {suma} -|- Cantidad: {cant_arboles}')
        # print(f'Árbol: {arbol} -|- Inclinación promedio: {inclin_prom}')
    # pprint(sorted(lista_inclinaciones_arboles, reverse=True)[0])
    maximo = sorted(lista_inclinaciones_arboles, reverse=True)[0]
    return maximo


def medidas_de_especies(especies, arboleda):
    diccionario = {}
    for especie in especies:
        lista_especie = [(float(arbol['diametro']), float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        diccionario[especie] = lista_especie
    return diccionario


def medidas_de_especie(especie, arboleda):
    lista = [(float(arbol['diametro']), float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com'] == especie]
    return lista


def main(argumentos):
    '''
    Función principal que llama a las demás (para cuando se levanta el programa
    por línea de comandos).
    '''
    # Com: Acá se procede a cargar los archivos según los argumentos recibidos por línea de comandos
    print(f'Programa de arboleda de Buenos Aires')
    print(f'El dataset será buscado en "../Data/arbolado-en-espacios-verdes.csv"')
    print(f'Modo de uso: python arboles_s4.py [<parque>] [<especie>] ')
    print(f'Si no se ingresan argumentos, se asume parque "GENERAL PAZ" y especie "Jacarandá"')
    print(f'Si se ingresa un solo argumento, este debe ser el nombre del parque y se asume especie "Jacarandá"')
    print(f'Con dos argumentos deben ser, como se dijo más arriba, parque y especie')
    if len(argumentos) == 0:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = 'GENERAL PAZ'
        especie = 'Jacarandá'
        print('Se asume Parque General Paz y especie Jacarandá')
    elif len(argumentos) == 1:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = argumentos[0]
        especie = 'Jacarandá'
        print('Se asume especie Jacarandá')
    elif len(argumentos) == 2:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = argumentos[0]
        especie = argumentos[1]
    else:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = 'GENERAL PAZ'
        especie = 'Jacarandá'
        print('Número de argumentos inválido, asumimos todo!')

    ##### EJERCICIOS #####

    # Ejercicio 4.30
    '''
    arboleda = leer_arboles(nombre_archivo)
    lista_altura_arboles = obtener_alturas(arboleda, especie)

    plt.hist(lista_altura_arboles, bins=50)
    plt.show()
    '''
    ##############################
    '''
    # Ejercicio 4.31
    arboleda = leer_arboles(nombre_archivo)
    lista_tuplas_especie = medidas_de_especie(especie, arboleda)
    # Acá lo que hice fue unzipear la lista de tuplas en las dos variables que quiero
    diam, altura = list(zip(*lista_tuplas_especie))

    # Detalle para el gráfico
    N = len(diam)
    area = (25 * np.random.rand(N)) ** 2
    colors = np.random.rand(N)
    plt.scatter(diam, altura, s=area, alpha=0.5, c=colors)
    plt.xlabel('Diámetro (cm)')
    plt.ylabel('Altura (m)')
    plt.title(f'Relación altura/diámetro para la especie {especie} en Buenos Aires')
    plt.show()
    '''
    ##############################

    # Ejercicio 4.32

    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    # pprint(medidas['Eucalipto'][0][0])

    # Eucalipto
    eucalipto = medidas['Eucalipto']
    diam1, altura1 = list(zip(*eucalipto))

    N = len(diam1)
    area = (25 * np.random.rand(N)) ** 2
    colors = np.random.rand(N)
    plt.xlabel('Diámetro (cm)')
    plt.ylabel('Altura (m)')
    plt.title(f'Relación altura/diámetro para la especie {especies[0]} en Buenos Aires')
    plt.scatter(diam1, altura1, s=area, alpha=0.5, c=colors)
    plt.savefig('graf_Eucalipto', dpi=300)
    plt.show()

    plt.clf()

    # Palo borracho rosado
    palo_borracho = medidas['Palo borracho rosado']
    diam2, altura2 = list(zip(*palo_borracho))

    N = len(diam2)
    area = (25 * np.random.rand(N)) ** 2
    colors = np.random.rand(N)
    plt.xlabel('Diámetro (cm)')
    plt.ylabel('Altura (m)')
    plt.title(f'Relación altura/diámetro para la especie {especies[1]} en Buenos Aires')
    plt.scatter(diam2, altura2, s=area, alpha=0.5, c=colors)
    plt.savefig('graf_Palo_Borracho.png', dpi=300)
    plt.show()

    plt.clf()

    # Jacarandá
    jacaranda = medidas['Jacarandá']
    diam3, altura3 = list(zip(*jacaranda))

    N = len(diam3)
    area = (25 * np.random.rand(N)) ** 2
    colors = np.random.rand(N)
    plt.xlabel('Diámetro (cm)')
    plt.ylabel('Altura (m)')
    plt.title(f'Relación altura/diámetro para la especie {especies[2]} en Buenos Aires')
    plt.scatter(diam3, altura3, s=area, alpha=0.5, c=colors)
    plt.savefig('graf_Jacaranda.png', dpi=300)
    plt.show()


###### INICIO DEL PROGRAMA ######
if __name__ == '__main__':
    main(sys.argv[1:])
