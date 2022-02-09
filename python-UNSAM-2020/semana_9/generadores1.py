# Ejercicio 9.4

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line


# for line in open('../Data/camion.csv'):
#     print(line, end='')

# for line in filematch('../Data/camion.csv', 'Naranja'):
#     print(line, end='')

string = 'hola, me llamo nestor y soy pastor'

print('pastor' in string)
