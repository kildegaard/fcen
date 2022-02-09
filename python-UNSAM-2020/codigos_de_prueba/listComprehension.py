import csv
from pprint import pprint as pp


nombre_archivo = 'D:/gitLab/pyunsam/Data/fecha_camion.csv'
# nombre_archivo = '../Data/fecha_camion.csv'
with open(nombre_archivo, 'rt') as file:
    filas = csv.reader(file)
    headers = next(filas)
    lista = [{key: value for key, value in zip(headers, fil)} for fil in filas if fil[0] == 'Naranja']
    # for fila in filas:
    #     print(fila)
    print(lista)
