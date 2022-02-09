import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Importamos los datos
var_x, var_y = np.loadtxt('dato.csv', delimiter=',', skiprows=1, unpack=True)
err_var_y = 1.1 * np.ones(len(var_y)) # ponemos que todos los var_y tiene 1.1 de error a modo de ej

# Graficamos los datos crudos con su error
plt.errorbar(var_x, var_y, yerr=err_var_y, fmt='o-k', label='Datos')

# Calculamos el ajuste
def f_ajuste(x, A, C): return A*np.exp(C*x)
popt, pcov = curve_fit(f_ajuste, var_x, var_y, sigma=err_var_y)
A, C = popt

# Declaramos nuestro nuevo dominio e imagen y graficamos el ajuste
new_var_x = np.linspace(min(var_x), max(var_x), 1000)
new_var_y = f_ajuste(new_var_x, A, C)
plt.plot(new_var_x, new_var_y, '-r', label='Ajuste exponencial')

# Títuo y labels
plt.title('Datos y Ajuste Exponencial', fontsize=16)
plt.xlabel('Variable 1', fontsize=14)
plt.ylabel('Variable 2', fontsize=14)


# Grid, legend, save y show
plt.grid(True)
plt.legend()
plt.savefig('ajuste_exponencial.png')
plt.show()

# Printiamos en pantalla los parámetros óptimos con sus errores
err_A, err_C = np.sqrt(np.diag(pcov))
print(f'A: {A} ± {err_A}')
print(f'C: {C} ± {err_C}')