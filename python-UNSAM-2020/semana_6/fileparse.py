# fileparse.py - Semana 6
import csv


def parse_csv(iterable, select: list = None, types: list = None, has_headers: bool = True, silence_errors: bool = False) -> dict:
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''

    if select and not has_headers:
        raise RuntimeError('Para seleccionar, necesito encabezados.')

    filas = csv.reader(iterable)

    if has_headers:
        encabezados = next(filas)
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for nfila, fila in enumerate(filas, start=1):
            hubo_error = False
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            # Si se especificaron tipos, modifica esas columnas.
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila)]
                except ValueError as error_capturado:
                    hubo_error = True
                    if not silence_errors:
                        print(f'Row {nfila}: No pude convertir {fila}')
                        print(f'Row {nfila}: Motivo: {error_capturado}')
            # Armar el diccionario
            if not hubo_error:
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
    else:
        registros = []
        for fila in filas:
            if not fila:
                continue
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = tuple(fila)
            registros.append(registro)

    return registros
