# Ejercicio 10.4 - Potencias

def es_potencia(n: int, b: int) -> bool:
    '''
    Devuelve True si n es potencia de b
    ej: es_potencia(8, 2) -> True
        es_potencia(70, 10) -> False
    '''
    res = False
    aux = n // b
    if n % b == 0 or n == 1:
        res = True
    else:
        aux = es_potencia(aux, b)
    return res


a = es_potencia(1, 2)
print(a)
