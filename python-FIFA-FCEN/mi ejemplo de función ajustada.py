import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt('dato.csv', delimiter=',', skiprows=1, unpack=True)
var_x, var_y = data

err_var_y = 1.1 * np.ones(len(var_y))


plt.errorbar(var_x, var_y, yerr=err_var_y, fmt='o-k', label='Datos')


def ajuste_lineal(x, A, C):
    return (x*A + C)


popt, pcov = curve_fit(ajuste_lineal, var_x, var_y, sigma=err_var_y)
A, C = popt

new_var_x = np.linspace(min(var_x), max(var_x), 1000)
new_var_y = ajuste_lineal(new_var_x, A, C)

plt.plot(new_var_x, new_var_y, '-r', label='Ajuste lineal')


# Títuo y labels
plt.title('Datos y Ajuste Exponencial', fontsize=16)
plt.xlabel('Variable 1', fontsize=14)
plt.ylabel('Variable 2', fontsize=14)


# Grid, legend, save y show
plt.grid(True)
plt.legend()
plt.savefig('ajuste_lineal.png')
plt.show()

# Printiamos en pantalla los parámetros óptimos con sus errores
err_A, err_C = np.sqrt(np.diag(pcov))
print(f'A: {A} ± {err_A}')
print(f'C: {C} ± {err_C}')

array1 = ['gus', 1, 2]
array2 = ['chu', 4, 5]
print(array1+array2)
