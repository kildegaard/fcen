# Inicios de recursión en Python
# %%
def factorial(n: int, str_tab: str = '', debug=False) -> int:
    """
    Función factorial

    Args:
        n (int): valor a ser calculado
        str_tab (str, optional): tabulador. Defaults to ''.
        debug (bool, optional): para ver resultados intermedios. Defaults to False.

    Raises:
        ValueError: n no debe ser negativo

    Returns:
        int: factorial de n
    """
    if 0 <= n <= 1:
        if debug:
            print(f'{str_tab} Llegué al caso base. n={n}')
        res = 1
    elif n > 1:
        if debug:
            print(f'{str_tab} Me meto un nivel. n={n}')
        f = factorial(n - 1, str_tab + '\t', debug)
        res = n * f
        if debug:
            print(f'{str_tab} Empiezo a volver. [[ n = {n} | res = {n} * {f} ]]')
    else:
        raise ValueError('n no puede ser negativo')
    return res


# %%
n = 5
respuesta = factorial(n, debug=True)
print(f'{n}! = {respuesta}')

# %%
n = 5
respuesta = factorial(n)
print(f'{n}! = {respuesta}')

# %%
