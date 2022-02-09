# Ejercicio 8.11 - Canguros buenos y malos (?)

class Canguro(object):

    def __init__(self):
        self.contenido_marsupio = []

    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)

    def __str__(self):
        return f'{self.contenido_marsupio}'
