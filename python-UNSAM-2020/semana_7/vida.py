# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 03:02:40 2020

Autor: Gustavo Kildegaard (gustavo.kildegaard@gmail.com)
"""
# Ejercicio 7.1

from datetime import datetime


def seg_vividos(fecha: str) -> float:
    """
    Toma una fecha en formato string y devuelve la cantidad de segundos que pasaron hasta la fecha

    Args:
        fecha (str): Fecha en formato dd/mm/aaaa

    Returns:
        float: cantidad de segundos pasados desde la fecha ingresada
    """
    var = datetime.strptime(fecha, '%d/%m/%Y')
    dif = datetime.now() - var
    return dif.total_seconds()


def print_seg(fecha: str) -> None:
    """
    Imprime por pantalla la fecha ingresada y los segundos transcurridos

    Args:
        fecha (str): Fecha en formato dd/mm/aaaa
    """
    s = seg_vividos(fecha)
    print(f'Fecha nacimiento: {fecha} - Segundos vividos: {s:,.0f}s')


# Inicio programa
fechas = ['02/06/1988', '18/03/1990', '24/10/1966', '23/10/1992']
for fecha in fechas:
    print_seg(fecha)
