# %% ##### Ejercicio 7.7 #####

# Empezamos con los imports necesarios
import os
import pandas as pd
import seaborn as sns

# %%
# Nombre de los archivos
dir = '../Data'
parque = 'arbolado-en-espacios-verdes.csv'
veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_parques = os.path.join(dir, parque)
fname_veredas = os.path.join(dir, veredas)
# %%
# Creación de los DataFrame iniciales
df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)

# %%
# Armamos subsets de los DF iniciales

columnas_parques = ['altura_tot', 'diametro']
especies_parques = ['Tipuana Tipu', 'Jacarandá mimosifolia']
df_parques_aux = df_parques[df_parques['nombre_cie'].isin(especies_parques)]
df_tipas_parques = df_parques_aux[columnas_parques].copy()

columnas_veredas = ['altura_arbol', 'diametro_altura_pecho']
especies_veredas = ['Tipuana tipu', 'Jacaranda mimosifolia']
df_veredas_aux = df_veredas[df_veredas['nombre_cientifico'].isin(especies_veredas)]
df_tipas_veredas = df_veredas_aux[columnas_veredas].copy()
# %%
# Renombramos las columnas de ambos subsets para que sean las mismas

columnas = ['altura', 'diametro_altura_pecho']
df_tipas_parques.columns = columnas
df_tipas_veredas.columns = columnas
# %%
# Agregamos columna ambiente a los df
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'
# %%
# Mergeamos ambos DataFrames
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# %%
# Graficamos los Box-Plot para diámetros y para alturas de las tipas
df_tipas.boxplot('diametro_altura_pecho', by='ambiente')
df_tipas.boxplot('altura', by='ambiente')
