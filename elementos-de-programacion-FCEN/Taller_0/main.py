# EP Poker - Taller 0 - Pequeños cambios para probar el Git Tortoise

import random as rnd

# Definimos las funciones del programa

def generarMazo(n):
    mazo = []    
    for cartas in range(13):        # Generé un único mazo con cartas del 1 al 13
        mazo.append(cartas+1)    
    mazo *= n                       # n Mazos
    rnd.shuffle(mazo)               # Lo mezclo
    
    return mazo

def jugar(m):                                            # m es el mazo que recibe la función
    suma = 0
    while suma >= 0 and suma < 21 and len(m) > 0:
        suma += m.pop(0)

    return suma

def jugar_varios(mazo, cant_jugadores):
    lista_suma_jugadores = []
    for jugador in range(cant_jugadores):
        lista_suma_jugadores.append(jugar(mazo))        # Voy guardando en la lista los resultados de la función suma para cada jugador

    return lista_suma_jugadores

def jugar_miedo(mazo):
    suma = 0    
    while suma < 19 and len(mazo) > 0:
        suma += mazo.pop(0)

    return suma

def jugar_borracho(m):
    suma = 0
    num_random = 1                                       # Lo pongo en 1 para que entre al while la primera vez
    while suma < 21 and num_random > 0.5 and len(mazo) > 0:
        suma += m.pop(0)
        num_random = rnd.random()
        
    return suma

    
def jugar_smart(m):
    suma = m.pop(0)
    while(suma < 21):
        num_random = rnd.random()
        flag = 0
        for valor in range(21):
            if suma == (valor+1) and num_random >= (1/21 * suma) and flag == 0:
                suma += m.pop(0)
                flag = 1                # No vuelve al if una vez hecha la suma; vuelve al while
    return suma
        
def comparar_estrategia(lista_jug):
    lista_comparativa = []
    while(len(mazo) > 0):
        num_jugador = 1                 # Es un contador para saber qué jugador está jugando
        print('Empezamos con', len(mazo), 'cartas.')
        for elements in lista_jug:
            if   elements == 0:
                print('Jugador', num_jugador, 'juega modo Normal')
                suma = jugar(mazo)
                lista_comparativa.append(suma)
                
            elif elements == 1:
                print('Jugador', num_jugador, 'juega modo Miedo')
                suma = jugar_miedo(mazo)
                lista_comparativa.append(suma)
                
            elif elements == 2:
                print('Jugador', num_jugador, 'juega modo Borracho')
                suma = jugar_borracho(mazo)
                lista_comparativa.append(suma)
                
            else:
                print('Jugador', num_jugador, 'juega modo Smart')
                suma = jugar_smart(mazo)
                lista_comparativa.append(suma)
            print('Puntaje obtenido:', suma)
            print('Restan', len(mazo), 'cartas.')
            num_jugador += 1
    
    return lista_comparativa


# Empieza el programa

mazo = generarMazo(2)

vector = [2, 2, 2, 2]

lista_varios_jugadores = comparar_estrategia(vector)