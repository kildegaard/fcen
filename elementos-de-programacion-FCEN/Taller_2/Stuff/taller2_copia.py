#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def main(argumentos):
    ''' Función principal de procesador de datos meteorólogicos '''
    
    
    ## --- PARTE 0: Procesamiento de argumentos
    ## Leemos los valores de los argumentos que nos dieron
    
    arch_entrada = argumentos[0]
    arch_salida  = argumentos[1]
    tam_ventana  = argumentos[2]
     
    if len(argumentos)> 3:
        metodo = argumentos[3]
    else:
        metodo = "def"
    
    ## Prueba para ver qué argumentos se recibieron por línea de comandos
    #print('I:',arch_entrada, ' O:', arch_salida, ' L:', tam_ventana, ' M:', metodo) # Prueba para ver los parámetros que llegaron
    
    
    ## --- PARTE 1: Lectura de los datos del archivo
    ## Nos encargamos de leer todo el archivo de entrada completo (de acuerdo al caso, podría leerlo de a segmentos, y no cargarlo completo en memoria)
    
    lineasDeEntrada = []                       # Aquí nos vamos a guardar toda la info del archivo de entrada
    with open(arch_entrada, 'r') as entrada: # Abre los archivos de entrada (en modo R:Read) y el de salida (en modo W:Write)
        for linea in entrada:
            linea = linea.strip('\n')             # Elimina el salto de línea del final
            camposDeLinea = linea.split(',')     # Se parte la cadena de la línea entera y se genera una lista
            lineasDeEntrada.append(camposDeLinea) # Se agrega la lista de campos de la línea a la lista de líneas completa
            # print(lineasDeEntrada)
    
    
    ## --- PARTE 2: Procesamiento y generación de la salida ---
    ## Con los datos cargados, ya se puede hacer el procesamiento 
    
    
    # print(lineasDeEntrada ) # Prueba para ver que se haya leído bien el archivo de entrada
    
    lineasDeSalida = []
    lineasDeSalida = procesarDatos(lineasDeEntrada, tam_ventana, metodo)
    # ...
    
     
            
    # --- PARTE 3: Escritura de archivo de salida ---
    if 0 < int(tam_ventana) <= len(lineasDeEntrada):            # Pongo esta condición para que no imprima archivo si el tam_ventana es mayor
        with open(arch_salida, 'w') as salida:                  # que la cantidad de datos a recorrer o menor que cero
            for lineaPorCampos in lineasDeSalida:
                print(",".join(lineaPorCampos), file=salida)

def concatenador(headers, matriz):
    contador = 0
    for lineas in matriz:
        lineas.insert(0, str(headers[contador]))
        contador += 1
        
    return matriz

def hayNA(linea):               # Función que me dice si una lista contiene NA
    esNA = False
    elemento = 0
    while not esNA and elemento < len(linea):
        if linea[elemento] == 'NA':
            esNA = True
        elemento += 1
        # for elemento in range(len(linea)):
            # if linea[elemento] == 'NA':
                # esNA = True
        
    return esNA

def prom(linea):                # Función que devuelve el promedio de una lista
    tempTotal = 0
    contador = 0
    for temp in linea:
        tempTotal += float(temp)
        contador += 1
    return str( f'{tempTotal / contador :.2f}' )

def procesarDatos(datosEntrada, tamVentana, metodo):
    """ Esta función se encarga de procesar los datos de entrada para generar la salida
        [[ COMPLETAR CON LA DESCRIPCIÓN PROPIA DE SU FUNCIÓN ]]
    
    Parámetros:
    datosEntrada ([string]): lista de líneas leída del archivo de entrada
    tamVentana (int): tamaño de la ventana de procesamiento
    metodo(string): método de procesamiento de los NA
    
    Devuelve:
    [string]: datos de salida procesados
        
    """
    datos = trasponerListaDeListas(datosEntrada)
    
    if int(tamVentana) > len(datos[0]) or int(tamVentana) <= 0:      # Coloco esta condición para quitarme de encima esta situación
        print('El tamaño de ventana seleccionado es incompatible con los datos')
        return ''
    else:
        timeStampsAux = datos.pop(0)         # Me armé una lista con los timestamps
        timeStamps = []
        for times in timeStampsAux:
            timeStamps.append(datetime.strptime(times, '%Y-%m-%dT%H:%M:%S'))    # Les doy el formato adecuado a todos los elementos
        
        tsVector = []          # En este array voy a meter todas los delta de tiempo para la ventana seleccionada
        # print(timeStamps)
        for ts in range(len(timeStamps) - int(tamVentana) + 1):
            # print(ts)
            tsVector.append(f'{(timeStamps[ts + int(tamVentana)-1]-timeStamps[ts]).total_seconds() :.2f}')
        # print(tsVector)
        
        # datosSalida = []      # Acá voy a guardar los datos de salida
        
        # Voy a crear la matriz en donde guardaré los datos de los promedios
        col = len(timeStamps) - int(tamVentana) + 1
        fil = len(datos)
        datosSalida = [[None] * col for i in range(fil)]
        
        if   metodo == 'def' or metodo == '':
            print('Método def')
                        
            numLinea = 0
            for lineas in datos:
                for indice in range(len(datos[0]) - int(tamVentana) + 1):
                    datosSalidaAux = datos[numLinea][indice:indice + int(tamVentana)]
                    if hayNA(datosSalidaAux):
                        datosSalida[numLinea][indice] = 'NA'
                    else:
                        datosSalida[numLinea][indice] = prom(datosSalidaAux)
                    
                numLinea += 1
                    # print(indice)
            
                   
        elif metodo == 'prom':
            print('Método prom')
            
            
        elif metodo == 'med':
            print('Método mediana')
        elif metodo == 'dist':
            print('Método dist')
        else:
            print('Método de tratamiento de los NA incorrecto')
            return ''   
        
        

        datosSalidaT = trasponerListaDeListas(datosSalida)          # Vuelvo a trasponer los datos
        datosSalidaFinal = concatenador(tsVector, datosSalidaT)     # Uno los deltaTimeStamps con los promedios calculados
        




        # datosSalida = datosEntrada
        
    
        return datosSalidaFinal


def trasponerListaDeListas(lista): 
	""" 
	Dada una lista de listas, la traspone como si tratara de una matriz. 
	Así, si se recibe una lista que contiene cinco (5) listas, y cada lista contiene tres (3) elementos,  
	esta función devolverá una lista que contendrá 3 listas, y cada lista contendrá 5 elementos. 
	
	Por ejemplo, si lista es [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] ]
	trasponerListaDeListas(lista) devolverá [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
	
	 
	Recibe: 
	    lista: [[]] - Una lista de listas que contiene elementos de algún tipo (e.g., int). Se espera que todas las sublistas tengan la misma longitud. 
	     
	Devuelve: 
	    result: [[]] - Una lista de listas, con la trasposición de la lista original. 
	 
	""" 
	cantFilas = len(lista[0]) 
	traspuesta = [[] for _ in range(cantFilas)] # Creo una lista que sólo contiene las listas vacías a llenar 
	 
	for pos in range(cantFilas): 
	    for sublista in lista:      
	        traspuesta[pos].append(sublista[pos]) 
	         
	return traspuesta 




# Sólo se ejecturará si el programa es ejecutado (esto es, no se usa con 'import taller2.py'), por ejemplo, por línea de comandos.
if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Se esperaban más argumentos:\n taller2.py arch_entrada arch_salida tam_ventana [metodo_na]")
        sys.exit(1)
    
    main(sys.argv[1:])
