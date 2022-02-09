def busqueda_secuencial_(lista, e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0  # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i, z in enumerate(lista):
        comps += 1  # sumo la comparación que estoy por hacer
        if z == e:
            pos = i
            break
    return pos, comps
