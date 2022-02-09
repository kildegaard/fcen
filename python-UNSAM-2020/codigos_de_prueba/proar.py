lista1 = [11, 22, 33, 44, 55]
lista2 = [1, 2, 3, 4, 5]
lista3 = [(valor1 + valor2) for valor1 in lista1 for valor2 in lista2]
lista4 = [(valor1 + valor2) for valor1, valor2 in zip(lista1, lista2)]
print(lista4)
