# vigilante.py
import os
import time

f = open('mercadolog.csv')
f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.5)   # Esperar un rato y
        continue          # vuelve al comienzo del while
    fields = line.split(',')
    nombre = fields[0].strip('"')
    precio = float(fields[1])
    volumen = int(fields[2])
    if volumen > 1000:
        print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
