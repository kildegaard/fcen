# Ejercicio 1.8 - Adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
mes = 0

while saldo > 0:
    if mes < 12:
        saldo = saldo * (1 + tasa/12) - pago_mensual - adelanto
        total_pagado += pago_mensual + adelanto
    else:
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado += pago_mensual
    mes += 1
    
    
print("El saldo final es \t ${:,.2f}.-".format(saldo))
print("El total pagado es \t ${:,.2f}.- al cabo de {} meses".format(total_pagado, mes))
