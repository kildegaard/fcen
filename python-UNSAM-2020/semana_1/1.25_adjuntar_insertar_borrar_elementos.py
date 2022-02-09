# Ejercicio 1.25 - Adjuntar, insertar y borrar elementos - LISTAS

lista_frutas = ['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Pera']

# Agregar 'mango'
lista_frutas.append('mango')

# Insertar 'Lima' como segundo elemento
lista_frutas.insert(1,'Lima')

# Borrar 'Mandarina'
lista_frutas.remove('Mandarina')

# Agregar 'Banana' al  final de la lista
lista_frutas.append('Banana')

# Encontrar la primera aparición de 'Banana'
print(lista_frutas.index('Banana'))
print(lista_frutas[4])

# Borrar la primera aparición de 'Banana'

# lista_frutas.remove(4) -> este no funciona así, es para borrar VALORES
del lista_frutas[4]


## EJECUCIÓN

print(lista_frutas)