# Ejercicio 1.28 - Listas de cualquier cosa

nums = [101, 102, 103]
lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']

items = ['spam', lista_frutas, nums]

print(items)

print('')

print(items[1])             # Accede al 2do elemento, que es una lista
print(items[1][4])          # Accede al 5to elemento de esa lista, que es un string
print(items[1][4][0])       # Accede al primer caracter del string