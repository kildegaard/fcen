import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# print(f"hola {np.e}")
# vec1 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# print(vec1)

# vector = np.linspace(0, 1, 11)
# print(vector)

# array_identidad = np.identity(5)
# print(array_identidad)

# array_eje = np.eye(5, k=2)
# print(array_eje)



# # EJERCICIO 1

# dominio = np.linspace(-5, 5, 20)
# print(dominio)
# imagen = dominio ** 2
# print(imagen)

# # EJERCICIO 1 BIS

# dominio_abs = np.abs(dominio)
# print(dominio_abs)


# # EJERCICIO 2

# matriz_en_linea = np.arange(1, 257, 1)
# print(matriz_en_linea)

# matriz_reshapeada = np.reshape ( matriz_en_linea, (16, 16))
# print(matriz_reshapeada)

# help(np.reshape)



# x = np.linspace(0, 2*np.pi,500)

# def f(x):
#     return np.sin(x)*np.sin(20*x)

# dominio = x
# imagen = f(x)

# plt.plot(dominio, imagen, '-r',label = "Artic Monkeys")
# plt.grid()
# plt.plot(dominio, 2*imagen,'-b', label = "Rammstein")
# plt.legend(loc=8)
# plt.title("Músicas")
# plt.xlabel("Dominio")
# plt.ylabel("Imagen")
# plt.show()

# plt.xlabel("Dominio")
# plt.ylabel("Imagen")
# plt.legend()
# plt.title("Gráfico copado")

# plt.plot(dominio,imagen)

# Para IMPORTAR DATOS

data = np.loadtxt('dato.csv',delimiter=',',unpack=True,skiprows=1)
print(data)