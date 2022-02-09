import lote

lote1 = lote.Lote('Pera', 100, 490.1)
print(f'Nombre: {lote1.nombre} - Cajones: {lote1.cajones} - Precio: $ {lote1.precio:.2f}')

print(lote1.costo())
lote1.vender(25)
print(lote1.costo())
