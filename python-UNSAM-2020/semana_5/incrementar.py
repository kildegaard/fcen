from pprint import pprint as pp


def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l - 1, -1, -1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n: int) -> list:
    """
    Función que genera todas las secuencias de longitud n

    Args:
        n (int): longitud de la lista

    Returns:
        list: lista de secuencias
    """
    lista = [0] * n
    lista_de_secuencias = []
    while 0 in lista:
        lista_de_secuencias.append(lista)
        lista = lista.copy()
        lista = incrementar(lista)
    else:
        lista_de_secuencias.append(lista)

    return lista_de_secuencias


# sec = [0, 0, 1, 0, 1, 1]
# sec_incr = incrementar(sec)
# print(sec_incr)

a = listar_secuencias(5)
pp(a)

# Esto que sigue acá fue para probar la idea de medir el tiempo de ejecución del programa
# Te tira el tiempo de ejecución y te grafica los mismos


import time
import matplotlib.pyplot as plt

record = []
cant_rep = 23

for reps in range(0, cant_rep):
    start = time.time()
    a = listar_secuencias(reps)
    end = time.time()
    tiempo = (end - start)
    record.append((reps + 1, round(tiempo, 4) * 1000))
    print(f'Ejecución #{reps+1:2d} - Tiempo: {tiempo:>7.4f} ms')

x, y = list(zip(*record))

plt.plot(x, y, label='listar secuencias')
plt.xlabel('Largo n de la secuencia')
plt.ylabel('Tiempo(s)')
plt.title('Gráfico de tiempo vs long de cadena')
plt.legend()
plt.show()
