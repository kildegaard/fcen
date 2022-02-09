class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def ruido(self):
        pass


class Perro(Animal):
    def __init__(self, nombre, color, raza):
        super().__init__(nombre)
        self.color = color
        self.raza = raza

    def ruido(self):
        print('Woof!')


class Gato(Animal):
    def __init__(self, nombre, color, raza):
        super().__init__(nombre)
        self.color = color
        self.raza = raza

    def ruido(self):
        print('Meooow!')


gato_1 = Gato('Chuzo', 'Blanco y negro', 'Genérico')
gato_1.ruido()
print(f'Gato | Nombre: {gato_1.nombre} | Color: {gato_1.color} | Raza: {gato_1.raza}')
gato_1.raza = 'Hermoso'
print(f'Gato | Nombre: {gato_1.nombre} | Color: {gato_1.color} | Raza: {gato_1.raza}')

perro_1 = Perro('Charlie', 'Marrón', 'Cocker')
perro_1.ruido()
