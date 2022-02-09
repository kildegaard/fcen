# Ejercicio 3.9 - Propagación

def propagar(vector):
    """
    Función que toma una lista de -1, 0 y 1 y devuelve otra, habiendo propagado
    los 1 a sus vecinos si estos son 0.

    Args:
        vector (list): lista de longitud cualquiera de -1, 0 y 1

    Returns:
        list: lista propagada
    """
    # Hago una copia para no pisar a v (sólo por obsesión)
    fosforos = vector.copy()
    iteraciones = 0
    # Este ciclo se repetirá (len(v) - 2) veces, con lo cual puedo recorrer toda la lista haciendo
    #  dos comparaciones por ciclo (una hacia adelante y otra hacia atrás)
    while iteraciones < (len(fosforos) - 2):
        # Recorro el vector desde la segunda posición hasta la anteúltima (así zafo de verificar si
        # es un extremo del mismo)
        for n in range(start=1, end=(len(fosforos) - 1)):
            # Acá se propaga el 1 hacia adelante y/o hacia atrás si se cumplen las condiciones
            if fosforos[n] == 1 and fosforos[n - 1] == 0:
                fosforos[n - 1] = 1
            if fosforos[n + 1] == 0:
                fosforos[n + 1] = 1
            else:
                continue
        iteraciones += 1
    return fosforos


# vector = [0, 0, 0, 1, 0, 0]
vector = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]

linea_de_fosforos = propagar(vector)
print(linea_de_fosforos)
