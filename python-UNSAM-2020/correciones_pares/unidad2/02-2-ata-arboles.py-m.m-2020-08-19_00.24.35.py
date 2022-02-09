#para ejercicio 2.22 lectura de los arboles de un parque, pegar en ejercicios_python y hacer correr desde ahi

import csv

#Err: Nombre de la función corresponde a los ejercicios previos, este es de árboles!
def leer_camion(nombre_archivo):
#Com: Espacios alrededor del =
    arboles=[]

    with open(nombre_archivo,'rt',encoding='utf8') as f:
        rows=csv.reader(f)
        headers=next(rows)
        for row in rows:
            ar=dict(zip(headers,row))
            arboles.append(ar)
    return arboles    
   
   
#Com: Conviene tener las definiciones al principio y luego todo el código externo
lista=leer_camion('Data/arbolado-en-espacios-verdes.csv')

lista_paz=[]
#Com: Nombres de variables poco descriptivos
for c in lista:
    if c['espacio_ve']=='GENERAL PAZ':
#Err: Sobra un espacio en la identación
         lista_paz.append(c)

#Com: "General Paz" está hardcodeado, podría haberse armado el programa para leer esto por línea de comandos
print('En el parque General Paz hay:',len(lista_paz),' arboles')
print()
#para ejercicio2.23
def especies(lista_arboles):

    especies=[]
    for e in lista_arboles:
          especies.append(e['nombre_com'])
    especies=set(especies)
    return especies

especies_arboles=especies(lista)
print(sorted(especies_arboles))

        
