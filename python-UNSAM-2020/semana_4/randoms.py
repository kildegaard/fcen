import random as rnd
from collections import Counter

# n_tiradas = 10
# dados = 5

# tiradas = [[rnd.randint(1, 6) for i in range(dados)] for j in range(n_tiradas)]
# print(tiradas)

lista = [1, 6, 4, 2, 3]

contar_dados = Counter(lista)
# print(contar_dados.most_common(2)[0][0])

max_num = max(contar_dados)
print(sorted(contar_dados)[0])
