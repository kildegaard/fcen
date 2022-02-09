def esConcava(lista):
    esConc = False
    contador = []
    if 0 <= len(lista) <= 2:                            # Me saco el problema de lista vacia, 1 y 2 elementos, que siempre es cóncavo
        esConc = True
    else:
        for valor in range(len(lista)-1):               # Con este for recorro la lista y marco los posibles cambios de inflexión
            if   lista[valor+1] < lista[valor]:
                contador.append('-')
            elif lista[valor+1] > lista[valor]:
                contador.append('+')
    
    if   contador.count('+') == 0 or contador.count('-') == 0:
        esConc = True                                   # Agarra los casos de todo positivo, todo negativo o meseta que son cóncavos
    elif contador.index('+') > contador.index('-'):     # Sería cóncavo A MENOS que luego vuelva a haber negativo ("firulete")
        contadorRecortado = contador[contador.index('+'):] 
        if contadorRecortado.count('-') == 0:           # Chequeo que luego de la situación [- - - +] (cóncavo) no haya otros - ("firulete")
            esConc = True         

    return esConc

def esConcava2(lista):
    esConc = True
    vieneDecreciendo = False
    vieneCreciendo = False
    for valor in range(len(lista)-1):               # Con este for recorro la lista y marco los posibles cambios de inflexión
        if   lista[valor+1] < lista[valor]:
            vieneDecreciendo = True
            if vieneCreciendo == True:
                esConc = False
        elif lista[valor+1] > lista[valor]:
            vieneCreciendo = True
        
    return esConc

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def hayEscalon(lista, l, h):
    hayE = False
    indiceH = 0
    indice = 0
    recorroL = True

    while recorroL == True and indice<(len(lista)-1):           # recorroL se hace False cuando atrasOK y adelanteOK se hacen True
                                                                # La segunda condición es para evitar que se vaya del rango
        if (lista[indice+1] - lista[indice]) == h:
            indiceH = indice                                    # Me guardo el índice que separa ambas partes de la lista
            # print(indiceH)
            if ( (l-1) < len(lista[:indiceH+1]) ) and ( (l-1) < len(lista[indiceH+1:]) ): # (l-1) es la cant. de iter. que realizaré.
                                                                                          # Chequeo que el largo de ambos tramos no superen
                                                                                          # la cantidad de iteraciones que voy a realizar
                                                                                          # para comprobar si los valores son iguales entre sí
                contadorOK = 0                                  # Contador de 'iteraciones que devolvieron igualdad entre los elementos de la lista
                atrasOK = False                                 # Banderita de que hacia atrás la longitud de elementos iguales es 'l'
                adelanteOK = False                              # Banderita de que hacia adelante la longitud de elementos iguales es 'l'
                for iter in range(l-1):
                    if lista[indiceH] == lista[indiceH - (iter+1)]:
                        contadorOK += 1
                if (l-1) == contadorOK:
                    atrasOK = True
                    # print('Atrás OK!')
                contadorOK = 0
                # print(lista[indiceH+1])
                for iter in range(l-1):
                    if lista[indiceH+1] == lista[(indiceH+1) + (iter+1)]:
                        contadorOK += 1
                # print(contadorOK)
                # print(l-1)
                if (l-1) == contadorOK:
                    adelanteOK = True
                    # print('Adelante OK!')

                if atrasOK == True and adelanteOK == True:      # Si para ambas direcciones la longitud es 'l' entonces HAY UN ESCALÓN
                                                                # DE LONGITUD L Y SALTO H
                    hayE = True
                    recorroL = False                            # Cambio a False para dejar de recorrer SI encontré lo que quiero
        indice += 1
    return hayE


# ~~~~~~~~~~~~Zona de prueba de funciones~~~~~~~~~~~~ #


# lista = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]
# lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# lista = [1, 1, 1, 1, 1]
# lista = []
# lista = [1]
# lista = [2, 4]
# lista = [4, 2]
# lista = [1, 1, 1, 0, -1, -2, -3, -2, -1, -10]

# print(esConcava(lista))


# lista = [1, 1, 1, 1, 1, 8, 8, 8, 8, 9]                # largo 3 escalon 7
# lista = [1, 5, 5, 5, 2, 2, 0]                         # largo 2 escalon -3
# lista = [1, 1, 1, 4, 4, 4, 4, 9, 9, 9, 9, 12, 12, 12]   # Varios largos mezclados

# largo = 3
# escalon = 3

# print(hayEscalon(lista, largo, escalon))

# lista = [5, 4, 3, 2, 1, 1, 1, 6, 8]     # True
# lista = [1, 2, 3, 4, 5, 5, 5, 5, 0]
# lista = [2, 1]
lista = [] 

print(esConcava2(lista))