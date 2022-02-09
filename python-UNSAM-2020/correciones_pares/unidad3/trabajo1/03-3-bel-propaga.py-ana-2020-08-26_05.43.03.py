# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:52:40 2020

@author: Anabela Lusi
"""

def propagar(lista):
    propagada = []
    for n, i in enumerate(lista): #Con el enumerate me guardo las posiciones
        try:
            if i == 1: #Si es 1 que guarde su valor
                propagada.append(lista[n]) 
                if lista[n-1]==0: #si a la izquierda del 1 hay 0
                    propagada.append(lista[n]) #entonces que guarde un 1
                if lista[n+1]==0: #si a la derecha del 1 hay 0
                    propagada.append(lista[n]) #entonces que guarde un 1
                if lista[n-1]==-1:  #Si a la izquierda hay -1
                    propagada.append(lista[n-1]) #Entonces que mantenga el -1
                if lista[n+1]==-1: #Si a la derecha hay -1
                    propagada.append(lista[n+1]) #Entonces que mantenga el -1

    #En el siguiente if, la idea es 'engancharlo cuando se completa el if anterior, pero no pude lograrlo!
                    if i == 0: #Si quedo algun cero me aseguro de que ahora no tengo un 1 al lado 
                        if lista[n-1]==1: 
                            propagada.append(lista[n-1])
                        if lista[n+1]==1:
                            propagada.append(lista[n+1])
                        else:
                            propagada.append(lista[n])
        except IndexError:
            continue #Esto es para que no corte el ciclo cuando quiere evaluar valores que se salen del rango
                
    return propagada #Me falta un valor.. es el primer cero que no se evalua nunca. Intento salvarlo con el if==0 pero no hay caso
            
x = propagar([0,0,1,-1,1])
x