# Mi codigo


# Ejercicio 8.11 - Canguros buenos y malos (?)

class Canguro(object):

    def __init__(self):
        self.contenido_marsupio = []

    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)

    def __str__(self):
        return f'{self.contenido_marsupio}'

## Codigo de canguro_malo corregido

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido = None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre

        if not contenido:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido

'''El error estaba en haber inicializado la lista en la definicion.
   De esta manera se creaba una sola vez y la misma era utilizada
   por todos los objetos en lugar de tener cada uno su propia variable'''
