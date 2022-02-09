import csv
import sys
import fileparse as fp


def leer_camion(archivo_camion):
    '''
    Esta función levanta un .csv con información del costo
    de cajones de fruta y devuelve una lista de tuplas con
    dicha información.
    ('nombre', 'cajones', 'precio')
    '''
    archivo = open(archivo_camion)
    tipos = [str, int, float]
    archivo_parseado = fp.parse_csv(archivo, types=tipos)
    return archivo_parseado


def leer_precios(archivo_precios):
    '''
    Esta función levanta un .csv con información del precio
    de venta de los cajones de fruta y verdura
    vendidos y devuelve un diccionario con dicha información.
    '''
    archivo = open(archivo_precios)
    tipos = [str, float]
    archivo_parseado = fp.parse_csv(archivo, types=tipos, has_headers=False)
    return archivo_parseado


def hacer_informe(archivo_camion, archivo_precios):
    '''
    return: lista de tuplas (nombre, cajones, precio, cambio)
    '''
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    informe = []
    for elemento in camion:
        cambio = round(dict(precios)[elemento['nombre']] - elemento['precio'], 2)
        frutas = (*elemento.values(), cambio)
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
    '''
    Función principal del programa que llama a todas las demás.
    '''
    if len(argumentos) == 1:
        archivo_camion = '../Data/camion.csv'
        archivo_precios = '../Data/precios.csv'
    elif len(argumentos) == 3:
        archivo_camion = argumentos[1]
        archivo_precios = argumentos[2]
    else:
        nom_archivo = argumentos[0]
        raise SyntaxError(f'Error de pasaje de argumentos\n{nom_archivo} ../camion.csv ../precios.csv')

    informe = hacer_informe(archivo_camion, archivo_precios)
    imprimir_informe(informe)


if __name__ == '__main__':
    main(sys.argv)
