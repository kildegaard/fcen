# -*- coding: utf-8 -*-

# Ejercicio 10.13 - Hojas ISO y recursión

def hojas(num):
    """
    Función recursiva que dado el valor de num devuelve el tamaño
    correspondiente de hoja A(num) en una tupla en mm
    Ej. si num = 0 -> (841, 1189)
        si num = 4 -> (210,  297)
    """
    if num == 0:
        ancho = 841
        largo = 1189
        res = ancho, largo
        return res
    else:
        ancho, largo = hojas(num - 1)
    return largo // 2, ancho

#################

num1 = 0
hoja_a0 = hojas(num1)

num2 = 4
hoja_a4 = hojas(num2)

print(f'Tamaño hoja A0: {hoja_a0[0]}mm por {hoja_a0[1]}mm.')
print(f'Tamaño hoja A4: {hoja_a4[0]}mm por {hoja_a4[1]}mm.')
