# %% ##### EJERCICIO 7.10 #####
import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

# %%
# Podemos hacer estas cosas porque le dijimos que parsee los dates! Muy piola
df['1-18-2014 9:00':'1-18-2014 18:00']
# %%
# Vamos a plotear un poco
df['12-25-2014':].plot()
# %%
dh = df['12-25-2014':].copy()
# %%
delta_t = -1  # tiempo que tarda la marea entre ambos puertos
delta_h = 18.5  # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
