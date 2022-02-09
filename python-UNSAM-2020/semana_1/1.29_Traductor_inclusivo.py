# Ejercicio 1.29 - Traductor (rústico) al lenguaje inclusivo

frase1 = 'todos somos programadores'
frase2 = 'Los hermanos sean unidos porque ésa es la ley primera'
frase3 = '¿cómo transmitir a los otros el infinito Aleph?'
frase4 = 'Todos, tu también'

palabras = frase2.split()

print(palabras)

frase_reformada = ''

for palabra in palabras:

# Este primer if tiene en consideración que no haya palabras de una sola letra
    if len(palabra) <= 1:
        frase_reformada += palabra + ' '
        continue
# Esta segunda parte tiene en cuenta las últimas 2 letras
    elif palabra[-2] == 'a' or palabra[-2] == 'o':
        palabra = palabra[:-2] + 'e' + palabra[-1:]
# Acá se tiene en cuenta la última letra
    elif palabra[-1] == 'a' or palabra[-1] == 'o':
        palabra = palabra[:-1] + 'e'

    frase_reformada += palabra + ' '
    

print(frase_reformada)