# Ejercicio 3.8

def invertir_lista(lista):
    """
    Función que invierte una lista y la devuelve.

    Args:
        lista (list]): Lista a invertir
    """
    lista_invertida = []
    for elemento in lista:
        lista_invertida.insert(0, elemento)
    return lista_invertida


lista1 = [1, 2, 3, 4, 5]
lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
lista3 = []

print(invertir_lista(lista1))
