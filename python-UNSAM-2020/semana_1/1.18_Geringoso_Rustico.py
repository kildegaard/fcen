# Ejercicio 1.15 - Concatenación de cadenas

# cadena = 'Geringoso'

# cadena = cadena.replace('a', 'apa')
# cadena = cadena.replace('e', 'epe')
# cadena = cadena.replace('i', 'ipi')
# cadena = cadena.replace('o', 'opo')
# cadena = cadena.replace('u', 'upu')

# print(cadena)

# # bien = 'Geperipingoposopo'
# # print(cadena == bien)

cadena = 'Geringoso'
cadena_nueva = ''

for char in cadena:
    if char.lower() == 'a':         # Le agrego el método .lower() para agarrar los casos también de mayúscula
        cadena_nueva += 'apa'       # Y acá voy armando el nuevo string reemplazando las vocales por sus
    elif char.lower() == 'e':       # análogos geringosos
        cadena_nueva += 'epe'
    elif char.lower() == 'i':
        cadena_nueva += 'ipi'
    elif char.lower() == 'o':
        cadena_nueva += 'opo'
    elif char.lower() == 'u':
        cadena_nueva += 'upu'
    else:
        cadena_nueva += char
print(cadena_nueva)
