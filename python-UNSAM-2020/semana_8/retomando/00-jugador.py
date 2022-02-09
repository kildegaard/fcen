# -*- coding: utf-8 -*-
# Empezando con objetos

class Jugador:
    """Clase jugador"""

    def __init__(self, X, Y):
        """Defino el constructor"""
        self.X = X
        self.Y = Y
        self.salud = 100

    def mover(self, dX, dY):
        """Mueve al personaje en dX, dY"""
        self.X += dX
        self.Y += dY

    def lastimar(self, pts):
        """Reduce la salud en pts"""
        self.salud -= pts


gus = Jugador(0, 0)

print(gus.salud)
gus.lastimar(10)
print(gus.salud)

print(f'Gus está en ({gus.X};{gus.Y})')

gus.mover(10, 15)
print(f'Gus está en ({gus.X};{gus.Y})')
