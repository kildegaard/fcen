#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:11:00 2020

@author: gus
"""
class ColaPrioridad:
    
    def __init__(self):
        """crea cola vacia"""
        self.items = []
        self.items_con_prioridad = []
        
    def encolar(self, x):
        """encola el elemetno x"""
        self.items.append(x)
        
    def encolar_prioritario(self, x):
        """encola al alemento x prioritario"""
        self.items_con_prioridad.append(x)
        
    def proximo(self):
        """devuelve el proximo elemtno sin desencolar
        REquiere que la cola no este vacia"""
        if len(self.items_con_prioridad) != 0:
            res = self.items_con_prioridad[0]
        else:
            res = self.items[0]
        return res
    
    def desencolar(self):
        """elimina el primer elemento de la cola"""
        if self.esta_vacia():
            raise ValueError
        
        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
        else:
            res = self.items.pop(0)
            
        return res
    
    def largo_cola(self):
        """devuelve el largo de ambas colas sumadas"""
        return len(self.items) + len(self.items_con_prioridad)
    
    def esta_vacia(self):
        return self.largo_cola() == 0
    
    def imprimir(self):
        res  = 'Normal: <'
        res += ', '.join(self.items)
        res += '>\n'
        res += 'Prioridad: <'
        res += ', '.join(self.items_con_prioridad)
        res += '>'
        
        if not self.esta_vacia():
            res += '\n'
            res += f'Proximo: {self.proximo()}'
        print(res)