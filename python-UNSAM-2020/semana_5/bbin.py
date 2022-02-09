# Versión modificada

def donde_insertar(lista: list, valor: int) -> int:
    """
    Función que devuelve la posición en la que debería poder insertarse un valor
    en una lista ordenada para que la misma continue ordenada

    Args:
        lista (list): lista (previamente ordenada)
        valor (int): valor a ser insertado

    Returns:
        int: posición del elemento a insertar
    """

    if valor < lista[0]:
        posicion = 0
    elif valor > lista[-1]:
        posicion = lista[-1]
    else:
        posicion = busqueda_binaria_modif(lista, valor, verbose=True)

    return posicion


def busqueda_binaria(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


def busqueda_binaria_modif(lista, x, verbose=False):
    '''Búsqueda binaria modificada
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    if pos == -1:
        pos = medio + 1
    return pos


def insertar(lista: list, elemento: int):
    pos = busqueda_binaria(lista, elemento)
    if pos != -1:
        posicion = pos
    else:
        posicion = busqueda_binaria_modif(lista, elemento)
        lista.insert(posicion, elemento)
    return posicion


# Funcionamiento del programa
'''
lista = [1, 2, 3, 4, 9, 10]
valor = 5
posic = insertar(lista, valor)

print(f'Valor: {valor}')
print(f'Posición: {posic}')
print(f'Lista: {lista}')
'''
