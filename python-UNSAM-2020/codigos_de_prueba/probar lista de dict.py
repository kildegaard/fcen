import os


def buscar_archivos_py():
    """busca archivos en el directorio actual y devuelve los .py

    Returns:
        list: lista de archivos .py
    """
    lista_archivos = os.listdir('.')
    lista_py = [{'num_archivo': narchivo, 'nom_archivo': archivos_py} for narchivo,
                archivos_py in enumerate(lista_archivos, start=1) if archivos_py[-3:] == '.py']

    return lista_py


# lista = buscar_archivos_py()
# # print(lista)
# for archivo in lista:
#     print(f'[{archivo["num_archivo"]}] - {archivo["nom_archivo"]}')

print(f'Leyendo archivos en este directorio...')
archivos_py = buscar_archivos_py()
print(f'Archivos encontrados:')
for archivo in archivos_py:
    print(f'[{archivo["num_archivo"]}] - {archivo["nom_archivo"]}')
eleccion = int(
    input(f'Qué archivo querés procesar? [Ingresá el número del mismo] > '))
path_archivo = archivos_py[eleccion - 1]['nom_archivo']

print(path_archivo)
