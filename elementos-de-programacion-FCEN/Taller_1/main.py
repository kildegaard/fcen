

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def hayEscalon(lista, l, h):
    hayE = False
    indiceH = 0
    indice = 0
    recorroL = True

    while recorroL == True and lista[indice]<len(lista):
        if (lista[indice+1] - lista[indice]) == h:
            indiceH = indice

            if ( (l-1) < len(lista[:indiceH+1]) ) and ( (l-1) < len(lista[indiceH+1:]) ):
                contadorOK = 0
                atrasOK = False
                adelanteOK = False
                for iter in range(l-1):
                    if lista[indiceH] == lista[indiceH - (iter+1)]:
                        contadorOK += 1
                if (l-1) == contadorOK:
                    atrasOK = True
                contadorOK = 0
                for iter in range(l-1):
                    if lista[indiceH] == lista[indiceH + (iter+1)]:
                        contadorOK += 1
                if (l-1) == contadorOK:
                    adelanteOK = True

                if atrasOK == True and adelanteOK == True:
                    hayE = True
                    recorroL = False
        indice += 1
    return hayE


# Zona de prueba de funciones


# lista = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]
# lista = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# lista = [1, 1, 1, 1, 1]
# lista = []
# lista = [1]
# lista = [2, 4]
# lista = [4, 2]
# lista = [1, 1, 1, 0, -1, -2, -3, -2, -1, -10]

# print(esConcava(lista))



