# Empezando con objetos

a = 2


class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts

    def leer_glob(self):
        print(a)


gus = Jugador(0, 0)
gus.leer_glob()
# print(x)
