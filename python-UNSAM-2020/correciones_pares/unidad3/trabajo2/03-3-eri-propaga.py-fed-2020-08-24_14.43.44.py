def propagar(lista):
    # Com: variables poco explicativas
    n = len(lista)-1
    j = 0
    for z in lista:
        if j < n:
            if lista[j] == 1 and lista[j+1] == 0:
                lista[j+1] = 1
        j += 1
    i = n
    for k in lista:
        if i > 0:
            if lista[i] == 1 and lista[i-1] == 0:
                lista[i-1] = 1
        i -= 1
    return lista


vector = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]

print(propagar(vector))
