# Ejercicio 1.9 - Calculadora de adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
mes = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
seguir = True               # Es un flag que utilizo para reconocer cuando saldo < pago_mensual

while saldo > 0 and seguir:
    mes += 1
    if (61 <= mes <= 108) and (saldo >= pago_mensual):              # Entrará acá cuando esté entre el 6to y 9no año
        saldo = saldo * (1 + tasa/12) - pago_mensual - adelanto
        total_pagado += pago_mensual + adelanto
    elif (saldo >= pago_mensual):
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado += pago_mensual
    else:
        seguir = False
        total_pagado += saldo
        saldo = 0
    
    print('Mes: {}  \t Total pagado: ${:>11,.2f} \t Saldo restante: ${:>11,.2f}'.format(mes, total_pagado,saldo))
    