def bubble_sort(lista):
    n = 0
    largo = len(lista)
    while largo:
        for j in range(largo - 1):
            print('pasada')
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
        largo -= 1
