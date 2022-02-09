import csv
from fileparse import parse_csv


def leer_camion(archivo_camion):
    '''
    Función que levanta un .csv
    '''
    tipos = [str, int, float]
    registros = parse_csv(archivo_camion, types=tipos)
    return registros


def leer_precios(archivo_precios):
    tipos = [str, float]
    registros = parse_csv(archivo_precios, types=tipos, has_headers=False)
    return registros


def hacer_informe(archivo_camion, archivo_precios):
    '''
    Recibe los path a los archivos .csv de Camión y de Precios.
    return: lista de tuplas (nombre, cajones, precio, cambio)
    '''

    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    informe = []
    for elemento in camion:
        fruta = [fruta for fruta in precios if fruta[0] == elemento['nombre']]
        cuenta = fruta[0][1] - elemento['precio']
        cambio = round(cuenta, 2)
        frutas = (*elemento.values(), cambio)
        informe.append(frutas)
    print(informe)

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


def informe_camion(archivo_camion, archivo_precios):
    """
    Función principal que llama a las demás.

    Los path se pueden pasar por línea de comandos. De no hacerlo, se asumen los
    archivos camion.csv y precios.csv para realizar el informe.
    """

    informe = hacer_informe(archivo_camion, archivo_precios)
    imprimir_informe(informe)


if __name__ == '__main__':
    archivo_camion = '../Data/camion.csv'
    archivo_precios = '../Data/precios.csv'

    informe_camion(archivo_camion, archivo_precios)
