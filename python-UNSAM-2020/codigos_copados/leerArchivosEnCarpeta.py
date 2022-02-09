import os
cosas = os.listdir('.')
cosasPy = [archivos_py for archivos_py in cosas if archivos_py[-3:] == '.py']
print(cosas)
print(cosasPy)
print(__file__)
