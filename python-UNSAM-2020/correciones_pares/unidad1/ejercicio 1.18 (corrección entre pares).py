#geringoso.py

cadena= 'BOLIGOMA'
capadepenapa= ''
for c in cadena:
    if c=='a':
         capadepenapa=capadepenapa + c +'pa'
    elif c=='e':
         capadepenapa=capadepenapa + c +'pe'
    elif c=='i':
         capadepenapa=capadepenapa + c +'pi'
    elif c== 'o':
         capadepenapa=capadepenapa + c +'po'
    elif c=='u':
         capadepenapa=capadepenapa + c +'pu'
    else:
        capadepenapa=capadepenapa + c

print(capadepenapa)

#resultado boligoma: bopolipigopomapa
