def print_call(func):
    def inner(*args, **kwargs):
        print('Llamando a {0} con argumentos {1} {2}'.format(func.__name__, args, kwargs))
        resultado = func(*args, **kwargs)
        print(f'El resultado fue {resultado}')
        return resultado
    return inner


# @print_call
def suma(a, b):
    sum = a + b
    return sum


@print_call
def conv_lista_en_tupl(lista1, lista2):
    lista = list(zip(lista1, lista2))
    return lista


l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

conv_lista_en_tupl(l1, l2)
