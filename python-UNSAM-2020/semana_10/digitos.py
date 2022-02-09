# Ejercicio 10.3 - Dígitos

def digitos(n: int) -> int:
    '''
    Función que recibe un n positivo y devuelve su cantidad de dígitos

    ej: n = 123456789 -> digitos(n) = 9
    '''
    if len(str(n)) == 0:
        dig = 0
    else:
        dig = 1 + digitos((str(n)[1:]))
    return dig


a = digitos(12345678900)
print(a)
