#!/usr/bin/env python3.
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:06:43 2020

@author: gustavo
"""
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_p = [elemento for subLista in lista for elemento in subLista]
