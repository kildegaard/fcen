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
    ## Nos encargamos de leer todo el archivo de entrada completo (de acuerdo al caso, podría leerlo de a segmentos, y no cargarlo completo en memoria
    
    lineasDeEntrada = []                       # Aquí nos vamos a guardar toda la info del archivo de entrada
    with open(arch_entrada, 'r') as entrada: # Abre los archivos de entrada (en modo R:Read) y el de salida (en modo W:Write)
        for linea in entrada:
            linea = linea.strip('\n')             # Elimina el salto de línea del final
            camposDeLinea = linea.split(',')     # Se parte la cadena de la línea entera y se genera una lista
            lineasDeEntrada.append(camposDeLinea) # Se agrega la lista de campos de la línea a la lista de líneas completa
    
    
    ## --- PARTE 2: Procesamiento y generación de la salida ---
    ## Con los datos cargados, ya se puede hacer el procesamiento 
    
    
    # print(lineasDeEntrada ) # Prueba para ver que se haya leído bien el archivo de entrada
    
    lineasDeSalida = procesarDatos(lineasDeEntrada, tam_ventana, metodo)
    # ...
            
    # --- PARTE 3: Escritura de archivo de salida ---
    with open(arch_salida, 'w') as salida:
        for lineaPorCampos in lineasDeSalida:
            print(",".join(lineaPorCampos), file=salida) # Guarda en un archivo los campos originales, sin la primera columna


def procesarDatos(datosEntrada, tamVentana, metodo):
    """ Esta función se encarga de procesar los datos de entrada para generar la salida
        [[ COMPLETAR CON LA DESCRIPCIÓN PROPIA DE SU FUNCIÓN ]]
    
    Parámetros:
    datosEntrada ([string]): lista de líneas leída del archivo de entrada
    tanVentana (int): tamaño de la ventana de procesamiento
    metodo(string): método de procesamiento de los NA
    
    Devuelve:
    [string]: datos de salida procesados
        
    """

    # Acá no se hace nada, pero deberán completar con su implementación
    datosSalida = datosEntrada
    # ---
    
    return datosSalida


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
