import lote

c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones', 'precio']

for colname in columnas:
    print(colname, '=', getattr(c, colname))

