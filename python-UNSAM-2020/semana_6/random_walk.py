import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo: int) -> list:
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def long_caminata(caminatas: list, calcula_max: bool) -> int:
    """
    Función que devuelve el índice de la caminata que más (o menos) se aparta del camino central

    Args:
        caminatas (list): lista de ndarray con las n caminatas realizadas al azar
        calcula_max (bool, optional): selector de si calculo máximo o mínimo. Defaults to True.

    Returns:
        int: Retorna el índice de la lista que cumple lo pedido
    """
    indice = 0
    alejamiento = 0
    for ncamin, caminata in enumerate(caminatas):
        cam = [abs(elemento) for elemento in caminata]  # Genero lista de valores absolutos para comparar más fácilmente

        if calcula_max:  # Entro acá (por default) para calcular el máximo apartamiento
            if max(cam) >= alejamiento:
                alejamiento = max(cam)
                indice = ncamin
        else:  # Entro acá si quiero calcular el mínimo apartamiento
            if ncamin == 0:  # Entro acá solo la primera vez
                alejamiento = max(cam)
                continue
            if max(cam) < alejamiento:
                alejamiento = max(cam)
                indice = ncamin
    return indice


def graficar(cant_caminatas: int, caminatas: list) -> None:
    fig = plt.figure(num=1, figsize=(10, 6), dpi=80, facecolor='grey', edgecolor='cyan', frameon=True)

    # Gráfico de las 12 caminatas
    plt.subplot(2, 1, 1)
    for caminata in caminatas:
        plt.plot(caminata)
    plt.xticks([])
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.title(f'{cant_caminatas} caminatas al azar')

    # Gráfico de la caminata que más se aleja
    plt.subplot(2, 2, 3)
    plt.plot(caminatas[long_caminata(caminatas, calcula_max=True)])
    plt.xticks([])
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.title(f'La caminata que más se aleja')
    plt.ylim(ymin=-700, ymax=700)

    # Gráfico de la caminata que menos se aleja
    plt.subplot(2, 2, 4)
    plt.plot(caminatas[long_caminata(caminatas, calcula_max=False)])
    plt.xticks([])
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.title(f'La caminata que menos se aleja')
    plt.ylim(ymin=-700, ymax=700)

    plt.show()


def main():
    """
    Función principal del programa
    """
    # Variables del problema
    N = 100000
    cant_caminatas = 12

    # Ejecución del mismo
    caminatas = [randomwalk(N) for i in range(cant_caminatas)]
    graficar(cant_caminatas, caminatas)


# INICIO DEL PROGRAMA

if __name__ == '__main__':
    main()
