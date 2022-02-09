import numpy as np
import random as rd
from pprint import pprint as pp

temp_normal = 37.5

# Características del termómetro
mu = temp_normal
desvio = 0.2

n_mediciones = 999

mediciones = np.array([round(rd.normalvariate(mu, desvio), 2) for mediciones in range(n_mediciones)])
# mediciones = [round(rd.normalvariate(mu, desvio), 2) for mediciones in range(n_mediciones)]
print(mediciones)
max_temp = max(mediciones)
min_temp = min(mediciones)
avg_temp = sum(mediciones) / n_mediciones
med_temp = sorted(mediciones)[int(n_mediciones/2) - 1]
print(f'Máx temp: {max_temp:.2f}\nMin  temp: {min_temp:.2f}\nTemp promedio: {avg_temp:.2f}\nMediana de temp: {med_temp:.2f}')

np.save('../Data/Temperaturas.npy', mediciones)
