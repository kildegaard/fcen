# -*- coding: utf-8 -*-
# Ejercicio 8.1 - Objetos como estructura de datos

class Lote:
    """
    Clase tipo Lote
    """

    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __repr__(self):
        salida = f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
        return salida

    def costo(self):
        return self.cajones * self.precio

    def vender(self, cant):
        self.cajones -= cant

# Estas variables de aca abajo las genere para facilidad mia
a = Lote('Pera', 100, 490.1)
b = Lote('Naranja', 50, 150.5)

lote = [a, b]
