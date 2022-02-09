# Ejercicio 2.2 - Lectura de un archivo de datos

archivo_entrada = '../Data/camion.csv'

with open(archivo_entrada, 'rt') as file:
    headers = next(file)

    data = []
    for linea in file:
        data.append(linea.strip().split(','))

costo_total = 0
for elemento in range(len(data)):
    costo_total += int(data[elemento][1]) * float(data[elemento][2])

print(f'Costo total: $ {costo_total:.2f}.-')