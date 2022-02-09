def valor_absoluto(n: float) -> float:
    """
    Función que retorna el valor absoluto de n.
    Pre: n es un número real
    Pos: regresa el valor absoluto de n

    Args:
        n (float): valor a calcularle su abs

    Returns:
        float: valor absoluto de n
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l: list) -> int:
    """
    Función que recibe una lista de numeros y devuelve la suma de aquellos
    que son pares.
    Pre: lista de números enteros no vacía
    Pos: devuelve un int resultado de sumar aquellos números pares de la lista

    Invariante: que exista e en la lista l en cada ciclo

    Args:
        l (list): lista de enteros

    Returns:
        int: suma de pares
    """
    res = 0
    for e in l:
        if e % 2 == 0:  # e es par
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    res = 0
    nb = b
    while nb != 0:
        print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n: int) -> int:
    """
    Conjetura de Collatz: dado un número inicial n, proceder a realizar la siguiente secuencia:
    * Si n es par, dividirlo por dos
    * Si n es impar, multiplicarlo por tres y sumarle 1
    El ciclo termina cuando n = 1.
    Finalmente, devuelve la cantidad de pasos que se necesitaron para tal fin.

    Pre: n número entero mayor que cero
    Pos: devuelve un entero que cuenta la cantidad de iteraciones

    Invariante: n tiene que permanecer mayor que 1 hasta el final de los ciclos.

    Args:
        n (int): entero positivo

    Returns:
        int: res valor de salida entero
    """
    res = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res += 1

    return res
