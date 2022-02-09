# %%
def calc(f, x, y):
    return f(x, y)


def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


# %%
calc(sum, 1, 2)

# %%
calc(sub, 5, 3)

# %%
calc(lambda x, y: x + y, 10, 20)

# %%
calc(lambda x, y: x - y, 55, 20)

# %%
'''Una función típica de programación funcional: MAP'''


def incr(x):
    return x + 1


lista = [1, 2, 3]

valores = list(map(incr, lista))
print(valores)

'''
La función map se podría escribir de manera estructurada de la siguiente forma:

def map(func, elements):
    results = []
    for elem in elements:
        results.append(func(elem))
    return results
'''
# %%
'''Otra función especial: FILTER'''

a = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(a))

'''
La función filtro recibe una función (acá le mandamos un lambda) y nos devuelve
una lista con los resultados si el resultado fue TRUE
'''

# %%
'''Otra función estrella: REDUCE'''

from functools import reduce

a = reduce(lambda accum, current: accum + current, [1, 2, 3], 0)
print(a)

'''
Esta función acumula y regresa un solo valor dada una secuencia y pasándole
cada valor a una función junto con el resultado hasta ese momento
'''
