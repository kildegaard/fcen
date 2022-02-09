# Ejercicio 3.6 y 3.7 de la unidad 3
# %%
# Ejercicio 3.6

def buscar_u_elemento(lista, elemento):
    """
    Función que busca un elemento en una lista.
    Si lo encuentra, devuelve su última posición.
    Caso contrario, devuelve -1.

    Args:
        lista (list): lista de valores en donde buscar
        elemento (int): elemento a buscar
    """
    respuesta = -1
    for pos, elem in enumerate(lista, start=1):
        if elem == elemento:
            respuesta = pos
    return respuesta


def buscar_n_elemento(lista, elemento):
    """
    Función que busca un elemento en una lista y todas sus apariciones.
    Devuelve el número de veces que aparece dicho elemento.
    Caso contrario, devuelve -1.

    Args:
        lista (list): lista de valores a buscar
        elemento (int): elemento a buscar
    """

    cant_apariciones = 0
    for elem in lista:
        if elem == elemento:
            cant_apariciones += 1
    return cant_apariciones


numeros = [1, 5, 3, 4, 5, 6, 7, 5, 9]
elemento = 5

# pos = buscar_u_elemento(numeros, elemento)

'''
if pos != -1:
    print(f'El número {elemento} está en la posición {pos} de la lista.')
else:
    print(f'No se encontró al elemento {elemento} en la lista.')
'''

'''
cant_apar = buscar_n_elemento(numeros, elemento)
print(f'El elemento {elemento} aparece en la lista {cant_apar} veces.')
'''
# %%
# Ejercicio 3.7


def maximo(lista):
    """
    Función que devuelve el máximo de una lista.

    Args:
        lista (list): lista de números
    """
    if len(lista) == 0:
        print('Lista vacía!')
        max = None
    else:
        max = lista[0]
        for numero in lista:
            if numero > max:
                max = numero
    return max


numeros = [-17, 2, 3, -24, 5, 6, 7, 8, 109]
numMax = maximo(numeros)
print(f'El número más grande de la lista es {numMax}.')
