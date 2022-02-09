# Árboles

import csv
import sys
from collections import Counter
from pprint import pprint


def armar_set_distritos(nombre_archivo):
    '''
    # Esta función me la armé para mí (me facilitaba ver los distritos)
    Función que recibe el archivo .csv de los árboles y devuelve un
    set con todos los distritos que hay en el mismo.
    '''
    with open(nombre_archivo, 'rt', encoding='utf-8') as file:
        filas = csv.reader(file)
        headers = next(filas)
        set_parques = set()
        for fila in filas:
            data = dict(zip(headers, fila))
            set_parques.add(data['espacio_ve'])
    return set_parques


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
        lista_especie = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        diccionario[especie] = lista_especie
    return diccionario


def main(argumentos):
    '''
    Función principal que llama a las demás (para cuando se levanta el programa
    por línea de comandos).
    '''
    # Com: Acá se procede a cargar los archivos según los argumentos recibidos por línea de comandos
    if len(argumentos) == 0:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = 'GENERAL PAZ'
        especie = 'Jacarandá'
        # print('Se asume Parque General Paz y especie Jacarandá')
    elif len(argumentos) == 1:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = argumentos[0]
        especie = 'Jacarandá'
        # print('Se asume especie Jacarandá')
    elif len(argumentos) == 2:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = argumentos[0]
        especie = argumentos[1]
    else:
        nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
        parque = 'GENERAL PAZ'
        especie = 'Jacarandá'
        # print('Número de argumentos inválido, asumimos todo!')

    ##### EJERCICIOS #####

    # Ejercicio 2.22
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    print(
        f'En el parque "{parque}" hay un total de {len(parque_leido)} árboles.')
    '''

    # Ejercicio 2.23
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    conj_especies = especies(parque_leido)
    print('Conjunto de especies en el parque leído')
    print('=======================================')
    pprint(conj_especies)
    '''

    # Ejercicio 2.24
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    diccionario = contar_ejemplares(parque_leido)
    print(
        f'Las 5 especies más comunes en el parque "{parque}" son las siguientes:')
    for nelemento, elemento in enumerate(diccionario.most_common(5), start=1):
        print(f'{nelemento}º -> {elemento[0]}: {elemento[1]} ejemplares.')
    '''

    # Ejercicio 2.25
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    lista_alturas = obtener_alturas(parque_leido, especie)
    try:
        altura_prom = round(float(sum(lista_alturas) / len(lista_alturas)), 2)
        print(max(lista_alturas))
        print(altura_prom)
    except ZeroDivisionError:
        print('No se han encontrado árboles de esta especie!')
    '''

    # Ejercicio 2.26
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    lista_inclinaciones = obtener_inclinaciones(parque_leido, especie)
    for narbol, inclin in enumerate(lista_inclinaciones, start=1):
        print(f'El árbol {narbol} tiene una inclinación de {inclin}º.')
    '''

    # Ejercicio 2.27
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    emi = especimen_mas_inclinado(parque_leido)
    print(
        f'El espécimen más inclinado del parque {parque} es {emi[1]} con una inclinación de {emi[0]}º.')
    '''

    # Ejercicio 2.28
    '''
    parque_leido = leer_parque(nombre_archivo, parque)
    especie_mas_incl = especie_promedio_mas_inclinada(parque_leido)
    print(
        f'La especie más inclinada, en promedio, del parque {parque} es {especie_mas_incl[1]} con una inclinación total de {especie_mas_incl[0]}º.')
    '''

    # Ejercicio 3.18
    '''
    arboleda = leer_arboles(nombre_archivo)
    '''

    # Ejercicio 3.19
    '''
    arboleda = leer_arboles(nombre_archivo)
    lista_alturas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    pprint(lista_alturas)
    '''

    # Ejercicio 3.20
    '''
    arboleda = leer_arboles(nombre_archivo)
    lista_alturas_y_diam = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    pprint(lista_alturas_y_diam)
    '''

    # Ejercicio 3.21
    '''
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    diccio = medidas_de_especies(especies, arboleda)

    pprint(diccio)
    '''


###### INICIO DEL PROGRAMA ######
if __name__ == '__main__':
    main(sys.argv[1:])
