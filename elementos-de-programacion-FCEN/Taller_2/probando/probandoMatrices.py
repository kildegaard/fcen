#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:19:09 2020

@author: gus
"""
# Matriz

matriz = [[]]

matriz[0] = [1, 2]
# matriz[0][0] = 2

# Las matrices se inicializan con "List Comprehension"

col = 2
fil = 3
datosSalida = [[None] * col for i in range(fil)]