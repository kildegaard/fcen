import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn as sns
sns.set()


def graficar(dominio, imagen, titulo, x, y):
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.plot(dominio, imagen, '-g')


def ajuste_lineal(x, A, B):
    return A * x + B


def ajuste_exp(x, A, B):
    return A * np.exp(x * B)


dias, casos_totales = np.loadtxt('covid.csv', delimiter=';', skiprows=1, unpack=True)

# np.set_printoptions(suppress=True)
# print(dias)
# print(casos_totales)

dia_cuarentena = 18

dias_antes_cuarentena = dias[:dia_cuarentena]
casos_antes_cuarentena = casos_totales[:dia_cuarentena]


dominio = dias_antes_cuarentena
imagen = casos_antes_cuarentena

popt, pcov = curve_fit(ajuste_exp, dominio, imagen)
A, C = popt
new_var_x = np.linspace(min(dias), max(dias), 1000)
new_var_y = ajuste_exp(new_var_x, A, C)

graficar(dias, casos_totales,
         "Gráfico de los casos totales en Argentina",
         "Días",
         "Casos totales")
plt.axvline(x=18, ls='--')
plt.text(10, 8000, 'Comienzo de la cuarentena')

plt.plot(new_var_x, new_var_y, ':r', label='Ajuste exp')
plt.legend()
plt.show()
