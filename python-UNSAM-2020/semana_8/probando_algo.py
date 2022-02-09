import formato_tabla
lista_tup = [('a', 1, 1.0), ('b', 2, 2.0), ('c', 3, 3.0)]

formateador = formato_tabla.FormatoTablaTXT()

for nombre, numero, flotante in lista_tup:
    data = [nombre, f'{numero}', f'{flotante:0.2f}']
    print(type(data[1]))
    formateador.fila(data)
