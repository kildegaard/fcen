# Ejercicio 1.15 - Concatenación de cadenas

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

frutas [0]  # 'M'

frutas[-1]  # 'i'

frutas[-37] # 'M', igual que el primer ejemplo

frutas = frutas + ',Pera'
print(frutas)

frutas = 'Melón,' + frutas
print(frutas)

cadena = 'Ejemplo con for'
letra = 'o'
cant_letra = 0

for caracter in cadena:
    if caracter == letra:
        cant_letra += 1
    print('Caracter:', caracter)
print('Cantidad de letras "' + letra + '": ' + str(cant_letra))


