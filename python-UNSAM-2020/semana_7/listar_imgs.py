import os
import sys


def recorrer(path: str, tipo: str = '') -> None:
    """
    Recorre un directorio e imprime los archivos que coinciden con el tipo de archivo buscado.

    Args:
        path (str): Path a recorrer
        tipo (str, optional): Extensión del tipo de archivo que se desea enumerar. Defaults to ''.
    """
    contador = 0
    for root, _, files in os.walk(path):
        for name in files:

            if name.endswith(tipo):
                contador += 1
                print(os.path.join(root, name))
    if tipo:
        print(f'Cantidad de archivos tipo {tipo} encontrados: {contador}.')
    else:
        print(f'Cantidad de archivos en el directorio: {contador}')


def main(argumentos: list) -> None:
    """
    Función principal

    Funcionamiento:
        python listar_imgs.py [<PATH> <TIPO>]
        Ejemplo: python listar_imgs.py ../Data/ordenar png
        El ejemplo asume una estructura de archivos tipo:

        pyunsam
        |-Data
        | |_ordenar
        |    |_archivos-dentro-de-la-carpeta-ordenar
        |_semana_7
          |_listar_imgs.py

    Nota:
    Si no se escribe ningún argumento, busca todos los archivos dentro del CWD
    Si se ingresa solo el PATH, busca todos los archivos independientemente de la extensión.

    Args:
        argumentos (list): Lista de argumentos
    """
    tipo = ''

    if len(argumentos) == 0:
        path = '.'
    elif len(argumentos) == 1:
        path = argumentos[0]
    elif len(argumentos) == 2:
        path = argumentos[0]
        tipo = argumentos[1]

    if 0 <= len(argumentos) <= 2:
        recorrer(path, tipo)


if __name__ == '__main__':
    main(sys.argv[1:])
