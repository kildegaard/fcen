#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:45:45 2020

@author: gus
"""
import random
from colaPracticando import Cola

nombres = ['angel', 'estebal', 'facundo',
           'gabriel', 'maria', 'mora', 'romina',
           'ruth', 'sofia', 'tomas']

random.shuffle(nombres)

cola_de_espera = Cola()

cola_de_espera.encolar(nombres[0])
cola_de_espera.imprimir()

cola_de_espera.encolar(nombres[1])
cola_de_espera.imprimir()

cola_de_espera.encolar(nombres[2])
cola_de_espera.imprimir()

atender_a = cola_de_espera.desencolar()
print(f'Paso {atender_a}')

cola_de_espera.imprimir()

atender_a = cola_de_espera.desencolar()
print(f'Paso {atender_a}')

cola_de_espera.imprimir()

atender_a = cola_de_espera.desencolar()
print(f'Paso {atender_a}')

cola_de_espera.imprimir()
