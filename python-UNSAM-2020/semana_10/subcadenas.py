# Ejercicio 10.5 - Subcadenas

def posiciones_de(frase: str, cacho: str) -> list:
    if cacho in frase:
        res = True
    return res


frase = 'Me pica fuertemente ue ue'
cacho = 'ue'

print(posiciones_de(frase, cacho))
