import os
import datetime
import time

camino = './jugandoConOS.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year=2017, month=9, day=21, hour=19, minute=51, second=0)
fecha_modifi = datetime.datetime(year=2012, month=9, day=24, hour=12, minute=9, second=24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
# os.utime(camino, (ts_acceso, ts_modifi))
os.utime(camino)

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))