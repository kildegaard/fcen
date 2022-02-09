# -*- coding: utf-8 -*-
# Ejercicio primero de la seccion 8.4
import math

class Punto():
    """Objeto tipo punto"""

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __repr__(self):
        return f'Punto({self.x1},{self.x2})'


    def __add__(self, B):
        res = Punto(self.x1 + B.x1, self.x2 + B.x2)
        return res

class Rectangulo():
    """Figura geometrica"""

    #   ·----------B
    #   |          |
    #   |          |
    #   A----------·

    #   A y B son objetos tipo Punto(x1, x2)


    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __str__(self):
        return f'Rectangulo formado por los puntos ({self.A.x1};{self.A.x2}) y ({self.B.x1};{self.B.x2})'

    def __repr__(self):
        return f'Rectangulo({self.A}, {self.B})'


    def base(self):
        """Calcula la base del rectangulo"""

        if self.A.x1 <= self.B.x1:
            res = self.B.x1 - self.A.x1
        else:
            res = self.A.x1 - self.B.x1
        return res

    def altura(self):
        """Calcula la altura del rectangulo"""

        if self.A.x2 <= self.B.x2:
            res = self.B.x2 - self.A.x2
        else:
            res = self.A.x2 - self.B.x2
        return res

    def area(self):
        """Calcula el area del rectangulo"""

        res = self.base()*self.altura()
        return res

    def desplazar(self, C):
        """Desplaza el rectangulo en C"""

       # self.A.x1 += C.x1
       # self.A.x2 += C.x2

       # self.B.x1 += C.x1
       # self.B.x2 += C.x2

        self.A += C
        self.B += C
