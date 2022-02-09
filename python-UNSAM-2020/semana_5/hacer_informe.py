import csv
import sys


def leer_camion(archivo_camion):
    '''
    Esta función levanta un .csv con información del costo
    de cajones de fruta y devuelve una lista de tuplas con
    dicha información.
    ('nombre', 'cajones', 'precio')
    '''
    with open(archivo_camion, 'rt') as file:
        filas = csv.reader(file)
        headers = next(filas)
        lista_camion = []
        for nfila, fila in enumerate(filas, start=1):
            try:
                lote = (fila[0], int(fila[1]), float(fila[2]))
                lista_camion.append(lote)
            except:
                print(f'LC.Error en fila {nfila} - {fila}')
    return lista_camion


def leer_precios(archivo_precios):
    '''
    Esta función levanta un .csv con información del precio
    de venta de los cajones de fruta y verdura
    vendidos y devuelve un diccionario con dicha información.
    '''
    with open(archivo_precios, 'rt') as file:
        filas = csv.reader(file)
        precios = {}
        for line in filas:
            try:
                precios[line[0]] = float(line[1])
            except IndexError:
                # Si encuentra una línea vacía, no quiero que haga nada.
                continue
    return precios


def hacer_informe(archivo_camion, archivo_precios):
    '''
    Recibe los path a los archivos .csv de Camión y de Precios.
    return: lista de tuplas (nombre, cajones, precio, cambio)
    '''

    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    informe = []
    for elemento in camion:
        cambio = round(precios[elemento[0]] - elemento[2], 2)
        frutas = (*elemento, cambio)
        informe.append(frutas)

    return informe


def imprimir_informe(informe):
    '''
    Función que imprime el informe de situación.
    Recibe un informe (lista de tuplas) y lo imprime elegantemente por pantalla
    '''
    header = ['Nombre', 'Cajones', 'Precio', 'Cambio']
    lineas = ['------', '-------', '------', '------']
    print(
        f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
    print(
        f'{lineas[0]:>10s} {lineas[1]:>10s} {lineas[2]:>10s} {lineas[3]:>10s}')

    for nombre, cajones, precio, cambio in informe:
        precio = '$' + str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


def main(argumentos):
    """
    Función principal que llama a las demás.

    Los path se pueden pasar por línea de comandos. De no hacerlo, se asumen los
    archivos camion.csv y precios.csv para realizar el informe.
    """
    if argumentos:
        archivo_camion = argumentos[0]
        archivo_precios = argumentos[1]
    else:
        archivo_camion = '../Data/camion.csv'
        archivo_precios = '../Data/precios.csv'

    informe = hacer_informe(archivo_camion, archivo_precios)
    imprimir_informe(informe)


##### INICIO PROGRAMA #####

if __name__ == '__main__':
    main(sys.argv[1:])
