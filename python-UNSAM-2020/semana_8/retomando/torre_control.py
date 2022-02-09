#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:31:59 2020

@author: gus
"""

# Ejercicio 8.12 - Torre de Control

class TorreControl:
    """
    Modelo de manejo de torre de control
    """
    
    def __init__(self):
        """Constructor"""
        
        self.arribo = []
        self.partida = []
        
    def nuevo_arribo(self, vuelo):
        """Encola un nuevo arribo
        Son prioritarios respectos de las partidas"""
        self.arribo.append(vuelo)
    
    def nueva_partida(self, vuelo):
        """Encola una nueva partida"""
        self.partida.append(vuelo)
    
    def ver_estado(self):
        """Muestra la situacion actual"""
        res  = 'Vuelos esperando para aterrizar: '
        res += ', '.join(self.arribo)
        res += '\n'
        res += 'Vuelos esperando para despegar: '
        res += ', '.join(self.partida)
        res += '\n'
        print(res)
    
    def asignar_pista(self):
        """Desencola los vuelos/arribos.
        Desencola prioritariamente los arribos y luego las partidas"""
        if self.esta_vacia():
            raise ValueError('No hay vuelos entrantes o salientes')
        
        if len(self.arribo):
            res = self.arribo.pop(0)
            print(f'El vuelo {res} aterrizo con exito')
        else:
            res = self.partida.pop(0)
            print(f'El vuelo {res} despego con exito')
                
    
    def total_vuelos(self):
        """devuelve la totalidd de vuelos"""
        return len(self.arribo) + len(self.partida)
    
    def esta_vacia(self):
        res = self.total_vuelos() == 0
        return res
    
##########################
