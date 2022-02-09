#  Ejercicio 2.1 - Preliminares sobre lectura de archivos
import os

# print(os.getcwd())

'''
El código a continuación abre un archivo y lo lee
entero, de pe a pa. Es una forma útil para cuando
tenés archivos pequeños
'''

# # with open('D:/gitLab/pyunsam/Data/camion.csv', 'rt') as file:
# with open('../Data/camion.csv', 'rt') as file:
#     data = file.read()

# print(data)
# print(type(data))

'''
Otra opción copada, para cuando tenés archivos más grandes, es 
abrirlo y leer línea por línea.
'''

with open('../Data/camion.csv', 'rt') as file:
    for line in file:
        print(line, end=' ~ ')