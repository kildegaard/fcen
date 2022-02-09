# Ejercicio 9.10 - Un pipeline más largo

from vigilante import vigilar
import csv
import formato_tabla
import informe


def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def elegir_columnas(rows, indices):
    for row in rows:
        yield [ row[index] for index in indices ]

def formateador(fila, fmt):
    if fmt == 'txt':
        header = [nombre for nombre in fila.keys()]
        for h in header:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(header))
        for elem in fila:
            yield f'{str(fila[elem]):>10s}'
    elif fmt == 'csv':
        pass

def ticker(camion_file, log_file, fmt = 'txt'):
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)
    '''for fila in filas:
        a = formateador(fila, fmt)
        for b in a:
            print(b, end='  ')
    '''
    for fila in filas:
        a = formateador(fila, fmt)
        print(a)
if __name__ == '__main__':
    file = 'mercadolog.csv'
    lines = vigilar(file)

    rows = parsear_datos(lines)

    for row in rows:
        print(row)
