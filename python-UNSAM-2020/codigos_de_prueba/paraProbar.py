# lista = []

# def modif_lista(listinha):
#     listinha.append('holis')

# print(lista)

# modif_lista(lista)

# print(lista)

# a = [1, 2, 3, 4, 5]
# print(type(a))
# a = str(a)
# print(type(a))
# print(a[0])

#################################

# dictio = {}

# dictio['nombre'] = 'Gustavo'

#################################

# import csv
# from pprint import pprint

# archivo_camion = '../Data/camion.csv'

# with open(archivo_camion, 'rt') as file:
#     filas = csv.reader(file)
#     headers = next(filas)
#     lista_dict = []
#     for nfilas, fila in enumerate(filas, start = 1):
#         try:
#             data =  dict(zip(headers, fila))
#             lista_dict.append(data)
#         except ValueError:
#             print(f'Error en fila {nfilas} - {fila}')
#     pprint(lista_dict)

# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)
# lista_tuplas = [tupla1, tupla2]

# print(tupla1[0])
# print(lista_tuplas[0])

# import random as rd

# lista = [10, 1, 5, 100, 3, 14]
# lista1 = [rd.randint(1, 6) for i in range(5)]
# print(max(lista1))

# num = 10

# for dato in num:
#     print('holi')

# tirada = []


# def es_generala(tirada):
#     """
#     Función que dada una tirada de n dados te devuelve si es o no generala

#     Args:
#         tirada (list): Lista de tirada de n dados

#     Returns:
#         bool: es o no generala
#     """
#     # Verifico que todos los dados sean igual al primero (all devuelve True si todos sus valores lo son)
#     esGen = all(tirada[0] == dado for dado in tirada) and len(tirada) == 5
#     return esGen


# print(es_generala(tirada))

# lista = [1, 2, 2, 3, 4]
# print(set(lista))

mano = [
    {
        'palo': 'oro',
        'valor': 12,
        'valor envido': 10
    },
    {
        'palo': 'oro',
        'valor': 1,
        'valor envido': 1
    },
    {
        'palo': 'oro',
        'valor': 4,
        'valor envido': 4
    }
]

# valor_ordenado = mano['valor'].sort()
# print(valor_ordenado)


def calcula_envido(mano):
    valor_envido = 0
    carta_1 = mano[0]
    carta_2 = mano[1]
    carta_3 = mano[2]
    if carta_1['palo'] == carta_2['palo'] == carta_3['palo']:
        lista_valores = sorted([carta['valor'] for carta in mano], reverse=True)
        print(lista_valores)

    elif carta_1['palo'] == carta_2['palo']:
        pass
    elif carta_1['palo'] == carta_3['palo']:
        pass
    elif carta_2['palo'] == carta_3['palo']:
        pass


calcula_envido(mano)
