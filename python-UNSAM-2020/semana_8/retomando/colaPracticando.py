#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:36:54 2020

@author: gus
"""

class Cola():
    
    def __init__(self):
        """Inicializo una cola vacia"""
        self.items = []
        
    def encolar(self, x):
        """Encola el elemento x"""
        self.items.append(x)
        
    def proximo(self):
        """Devuelve el proximo elemento sin desencolar
        Requiere que la cola no este vacia"""
        return self.items[0]
    
    def desencolar(self):
        """Elimina el primer elemento de la cola y 
        devuelve su valor.
        Si la cola esta vacia levanta ValueError"""
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)
    
    def largo_cola(self):
        """Devuelve el largo de la cola"""
        return len(self.items)
    
    def esta_vacia(self):
        """Devuelve
        True si la cola esta vacia,
        False si no"""
        res = self.largo_cola() == 0
        return res
    
    def imprimir(self):
        """Imprime por pantalla la data"""
        res = '<'
        res += ', '.join(self.items)
        res += '>'
        if not self.esta_vacia():
            res += '\n'
            res += f'Prox: {self.proximo()}'
        print(res)