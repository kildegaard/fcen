# vigilante.py
import os
import time
import informe

def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

if __name__ == '__main__':
    for line in vigilar('mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        '''
        if volumen > 1000:
            res = f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}'
            print(res)
        '''

        camion = informe.leer_camion('../../Data/camion.csv')
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

