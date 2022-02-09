# Ejercicio 10.2

def ntriang(desde: int, hasta: int, str_tab: str = '', debug: bool = False) -> int:
    """
    Función que genera un número triangular entre [desde, hasta]

    Args:
        desde (int): Desde
        hasta (int): Hasta
        str_tab (str, optional): Defaults to ''.
        debug (bool, optional): Poner True para ver los niveles. Defaults to False.

    Returns:
        int: Número triangular
    """
    if desde <= hasta:
        if debug:
            print(f'{str_tab} Me meto un nivel')
        suma = desde + ntriang(desde + 1, hasta, str_tab + '  ', debug)
    else:
        suma = 0
        if debug:
            print(f'{str_tab} Llegué al caso base')
    if debug:
        print(f'{str_tab} Estoy saliendo')
    return suma


a = ntriang(0, 10, debug=False)
print(a)

b = ntriang(-10, 11)
print(b)
