# Gustavo Kildegaard - gustavo.kildegaard@gmail.com - 20-8-2020

'''
Funcionalidad: facilitar la lectura de los comentarios de un programa.
1. Lee un archivo .py
2. Guarda las líneas que comienzan con #
3. Separa en una lista si la línea comienza con # Err (error), # Com (comentario) o # (comentario del usuario).
4. Genera un informe.txt con la data.

USO:

python grabarComentarios.py <path/al/archivo.py>

Nota: Para que funcione adecuadamente, seguir las siguientes indicaciones:

* Los comentarios del usuario deben comenzar con # (aún no funciona con comentarios en bloque).
* Al corregir el código, comentar con # Err: <COMENTARIO> si se encuentra algún error.
* Al corregir el código, comentar con # Com: <COMENTARIO> si se quiere hacer alguna sugerencia al código, pero 
éste funciona adecuadamente.
'''

import sys
import os
from pprint import pprint


def leer_archivo(archivo_python):
    '''
    Función que levanta el .py y lo convierte en lista de strings.
    parámetro: file - archivo.py
    return: lineas - lista de strings
    '''
    lista_lineas = []
    with open(archivo_python, 'rt', encoding='UTF-8') as file:
        for raw_lineas in file:
            lineas = raw_lineas.strip().strip('\n')
            lista_lineas.append(lineas)
    return lista_lineas


def esComentario(linea):
    '''
    Función que determina si una línea leída es o no comentario.
    input: linea - string
    output: resultado - boolean
    '''
    resultado = False
    if linea.startswith('#') == True:
        resultado = True
    return resultado


def esComentarioMedio(linea):
    """
    Función que detecta comentarios en el medio de una línea.

    Args:
        linea (string): línea extraída del código para analizar.

    Returns:
        boolean: es o no un comentario!
    """
    res_bool = False
    res_nletra = 0
    for nletra, letra in enumerate(linea):
        # continue
        if letra == '#':
            res_bool = True
            res_nletra = nletra
    resultado = (res_nletra, res_bool)
    return resultado


def pre_procesamiento(lineas):
    '''
    Función que recibe la lista de lineas totales del programa leído y
    retorna una lista de tuplas (nlinea, linea) si la línea leída es un
    comentario.
    input: lineas - lista de strings
    output: lineas_de_comentario - lista de tuplas
    '''
    lineas_de_comentario = [(nlinea, comentario) for nlinea, comentario in enumerate(lineas, start=1)
                            if (esComentario(comentario) == True or esComentarioMedio(comentario)[1] == True)]

    lista_comentarios = []
    for tupla in lineas_de_comentario:
        diccionario = {}
        diccionario['num_linea'] = tupla[0]

        if esComentarioMedio(tupla[1])[1]:
            diccionario['comentario'] = tupla[1][esComentarioMedio(tupla[1])[
                0]:]
        else:
            diccionario['comentario'] = tupla[1]

        lista_comentarios.append(diccionario)
    return lista_comentarios


def procesar_lineas(lineas):
    '''
    Función que recibe una lista de diccionarios con la info del
    número de línea y comentario en sí y separa en tres listas distintas
    de acuerdo a si son comentarios del usuario, #Err o #Comm.
    input: lineas - lista de diccionarios
    output: userCom, errorCom, comCom - listas de diccionarios
    '''
    lista_errorcom = []
    lista_com = []
    lista_usercom = []
    for linea in lineas:
        if linea['comentario'].startswith('# Err'):
            lista_errorcom.append(linea)
        elif linea['comentario'].startswith('# Com'):
            lista_com.append(linea)
        else:
            lista_usercom.append(linea)
    return lista_errorcom, lista_com, lista_usercom


def buscar_archivos_py():
    """busca archivos en el directorio actual y devuelve los .py en forma de lista de dict

    Returns:
        list: lista de archivos .py
    """
    lista_archivos = os.listdir('.')
    lista_py = [{'num_archivo': narchivo, 'nom_archivo': archivos_py} for narchivo,
                archivos_py in enumerate(lista_archivos, start=1) if archivos_py[-3:] == '.py']

    return lista_py


def crear_informe(listErr, listCom, listUser, ingreso):
    '''
    Función que, finalmente, crea un archivo informe.txt con la información extraída de los comentarios.
    Primero imprime los comentarios del corrector, luego los errores y finalmente, los comentarios del usuario.
    input: err, com, user - listas de diccionarios
    '''

    nombre_archivo_salida = 'Informe_comentarios.txt'
    try:
        with open(nombre_archivo_salida, 'wt', encoding='UTF-8') as output:

            print(f'Informe del archivo {ingreso}', file=output)
            print('=' * (20 + len(ingreso)), file=output)

            print('', file=output)

            print('Lista de comentarios de mejora del corrector', file=output)
            print('********************************************\n', file=output)
            for com in listCom:
                print(f'Línea {com["num_linea"]}', '\t',
                      f'{com["comentario"][6:]}', file=output)

            print('', file=output)

            print('Lista de comentarios sobre errores del corrector', file=output)
            print('************************************************\n', file=output)
            for com in listErr:
                print(f'Línea {com["num_linea"]}', '\t',
                      f'{com["comentario"][6:]}', file=output)

            print('', file=output)

            print('Lista de comentarios del autor', file=output)
            print('******************************\n', file=output)
            for com in listUser:
                print(f'Línea {com["num_linea"]}', '\t',
                      f'{com["comentario"][1:].strip()}', file=output)
        print('Se creó exitosamente el archivo informe.txt')
    except:
        print('Hubo algún error!')


def main(argumentos):
    '''
    Función principal del programa
    '''
    run = False
    if len(argumentos) == 0:
        print(f'Leyendo archivos en este directorio...')
        archivos_py = buscar_archivos_py()
        if len(archivos_py) == 1:
            print('No se encontró ningún archivo .py!')

        elif len(archivos_py) == 2:
            print(__name__)
            nombre_archivo_grabar = __file__  # Esto funciona!

            '''Esto de más abajo lo había puesto porque se supone que en la
            variable __file__ se guardaba TODA la ruta del archivo... pero aparentemente
            no... wtf'''
            # index_ultimo_slash = len(__file__) - __file__[::-1].index('/')
            # nombre_archivo_grabar = __file__[index_ultimo_slash:]

            for archivo in archivos_py:
                if nombre_archivo_grabar not in archivo['nom_archivo']:
                    path_archivo = archivo['nom_archivo']
            run = True
        else:
            print(f'Archivos encontrados:')
            for archivo in archivos_py:
                print(f'[{archivo["num_archivo"]}] - {archivo["nom_archivo"]}')
            eleccion = int(
                input(f'Qué archivo querés procesar? [Ingresá el número del mismo]'))
            path_archivo = archivos_py[eleccion - 1]['nom_archivo']
            run = True
    elif len(argumentos) == 1:
        path_archivo = argumentos[0]
        run = True
    else:
        print('Error en el ingreso de los argumentos!')
        print('python grabarComentarios.py <path/del/archivo.py>')

    if run:

        lineas = leer_archivo(path_archivo)
        lineas_de_comentario = pre_procesamiento(lineas)
        lista_errorcom, lista_com, lista_usercom = procesar_lineas(
            lineas_de_comentario)
        crear_informe(lista_errorcom, lista_com, lista_usercom, path_archivo)


##### INICIO DEL PROGRAMA #####
if __name__ == '__main__':
    main(sys.argv[1:])
