def sumar_enteros_ciclo(desde: int, hasta: int) -> int:
    """
    Función que calcula la suma en el intervalo [desde, hasta].
    Si hasta < desde, devuelve 0

    Args:
        desde (int): valor desde el cual se comienza a sumar
        hasta (int): valor hasta el cual se procede a la suma

    Returns:
        int: suma de los valores en el intervalo cerrado

    Contrato
    ********
    Pre: desde menos que hasta, ambos enteros
    Pos: devuelve un entero que es la suma del intervalo. Si el intervalo es
    vacío, devuelve 0
    """
    if hasta > desde:
        suma = sum([x for x in range(desde, hasta + 1)])
    else:
        suma = 0
    return suma


def sumar_enteros(desde: int, hasta: int) -> int:
    """
    Función que calcula la suma en el intervalo [desde, hasta].
    Si hasta < desde, devuelve 0

    Args:
        desde (int): valor desde el cual se comienza a sumar
        hasta (int): valor hasta el cual se procede a la suma

    Returns:
        int: suma de los valores en el intervalo cerrado

    Contrato
    ********
    Pre: desde menos que hasta, ambos enteros
    Pos: devuelve un entero que es la suma del intervalo. Si el intervalo es
    vacío, devuelve 0
    """
    if hasta > desde:
        suma_desde = ((desde - 1) * (desde)) / 2
        suma_hasta = (hasta * (hasta + 1)) / 2
        suma = suma_hasta - suma_desde
    else:
        suma = 0
    return int(suma)
