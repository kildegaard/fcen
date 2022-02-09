# solucion_de_errores.py
# Ejercicios de errores en el código

# %%
# Ejercicio 3.1
'''
Error:
El error en este ejercicio es de tipo semántico. El while solo correrá una vez debido a que ambas opciones del if/else
tienen un return, de modo que luego del primer ciclo se sale de la función.

Solución:
Esto se soluciona bajando dos niveles de identación la cláusula |return False| para que esté a la altura del while.

### CÓDIGO CORREGIDO ###
'''


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

# %%
# Ejercicio 3.2
'''
Error:
Hay varios errores en el código de tipo sintáctico.
1. Faltan los : luego del nombre de la función
2. Faltan los : luego del while
3. Faltan los : luego de la expresión del if
4. En la guarda del if se usó = (asignación) en lugar de == (comparación)
5. El último return devuelve "Falso" que es una variable que no existe en la función, probablemente se quiso
poner return False

### CÓDIGO CORREGIDO ###
'''


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

# %%
# Ejercicio 3.3
'''
Error:
En el código hay un error de tipo. La variable expresion espera recibir un string (tipo que acepta el método len()).
Sin embargo, en el tercer ejemplo se le pasa como argumento 1984 que es de tipo entero.


### CÓDIGO CORREGIDO ###
'''


def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

# %%
# Ejercicio 3.4
'''
Error:
El problema con este ejemplo es la ausencia del return en la función suma. Efectivamente, dentro de la función suma
existe una variable c de tipo entero que evalúa a 5, pero al no tener un return, este valor queda dentro del scope
de la función en sí, no existe fuera de ella.

### CÓDIGO CORREGIDO ###
'''


def suma(a, b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")

# %%
# Ejercicio 3.5
'''
Error:
Este es un error que me pasó cuando estaba haciendo el ejercicio en la unidad anterior. Me hizo pensar mucho porque
a primera vista estaba todo bien. Sin embargo, lo solucioné poniendo la línea registro = {} dentro del for, y no fuera.
De esta forma, cada vez que hago un nuevo ciclo borro el contenido del mismo.
Me resulta extraña la idea de por qué no simplemente se sobreescribe, pero como decía al final del ejercicio, es algo
que veremos un poco más adelante!

### CÓDIGO CORREGIDO ###
'''

from pprint import pprint
import csv


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion


camion = leer_camion("../Data/camion.csv")
pprint(camion)

# %%
