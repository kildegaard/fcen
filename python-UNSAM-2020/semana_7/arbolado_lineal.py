# %% ##### Ejercicio 7.7 #####

# Empezamos con los imports necesarios
import os
import pandas as pd
import seaborn as sns

# %%
# Nombre del archivo
dir = '../Data'
file = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(dir, file)

# %%
# Creamos el DataFrame
df = pd.read_csv(fname, low_memory=False)

# %%
# Quiero un subset de mi DataFrame inicial con estas columnas
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

df_lineal = df[cols_sel].copy()
df_lineal['nombre_cientifico'].value_counts()[0:10]
# %%
# Vamos a trabajar con estas especies seleccionadas:
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

# %%
# Volvemos a crear un subset, ahora con ciertas especies seleccionadas
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)].copy()
df_lineal_seleccion.head(10)

# %% ##### Ejercicio 7.8 #####

df_lineal_seleccion.boxplot('altura_arbol', by='nombre_cientifico')
# %%
# Otro gráfico lindo
sns.pairplot(data=df_lineal_seleccion[cols_sel], hue='nombre_cientifico')

# %%
