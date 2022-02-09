# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:31:23 2020

@author: Gustavo Kildegaard
@mail: gustavo.kildegaard@gmail.com
"""
# %%
import datetime
# %%
fecha_hora = datetime.datetime.now()
print(fecha_hora)
# %%
fecha = datetime.date.today()
print(fecha)
# %%
nacim_gus = datetime.date(year=1988, day=2, month=6)
nacim_agus = datetime.date(year=1990, day=18, month=3)
hoy = datetime.date.today()
dif1 = hoy - nacim_gus
dif2 = hoy - nacim_agus
años1 = (dif1 / 365.2425).days
meses1 = (dif1.days / 365.2425 - (dif1 / 365.2425).days) * 12
años2 = (dif2 / 365.2425).days
meses2 = (dif2.days / 365.2425 - (dif2 / 365.2425).days) * 12
print(f'Gus: {años1} años y {meses1:.0f} meses.')
print(f'Agus: {años2} años y {meses2:.0f} meses.')
# %%


def edad(dia: int, mes: int, anio: int) -> list:
    import datetime
    nacim = datetime.date(year=anio, day=dia, month=mes)
    hoy = datetime.date.today()
    dif = hoy - nacim
    edad = []
    edad.append((dif / 365.2425).days)
    edad.append(int((dif.days / 365.2425 - (dif / 365.2425).days) * 12))
    return edad


def print_edad(nombre: str, edad: list):
    print(f'{nombre}: {edad[0]} años y {edad[1]} meses.')


# %%
hoy = datetime.datetime.now()
fecha_random = datetime.datetime(1990, 3, 18, 15, 0, 0)
fecha_random - hoy
# %%
from datetime import *

a = time(0, 30, 0)
b = time(0, 45, 0)
