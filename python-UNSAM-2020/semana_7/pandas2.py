# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:21:16 2020

Autor: Gustavo Kildegaard (gustavo.kildegaard@gmail.com)
"""

#%%
import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

#%%
s2.plot()
#%%
# Ploteamos usando una media movil
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w, min_periods=1).mean()
s3.plot()

#%%
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()