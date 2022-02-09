# Ejercicio 1.7 - Hipoteca

saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1 + tasa/12) - pago_mensual
    total_pagado += pago_mensual
    
    
print("El saldo final es \t ${:,.2f}.-".format(saldo))
print("El total pagado es \t ${:,.2f}.-".format(total_pagado))
# print("El total pagado es ${:<20,.2f}.-".format(total_pagado))
# print("El total pagado es ${:^20,.2f}.-".format(total_pagado))
