class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}'

    def __repr__(self):
        return f'Persona({self.nombre}, {self.edad}, {self.nacionalidad})'


gus = Persona('Gustavo', 32, 'argentino')
