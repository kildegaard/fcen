# %%
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'

fname = os.path.join(directorio, archivo)

df = pd.read_csv(fname)
# %%
df.head(2)
# %%
df.columns
# %%
df.describe()
# %%
df.loc[df['diametro'].idxmax()]
# %%
# Qué árbol tiene el mayor diámetro?
df.loc[df['diametro'].idxmax()]
# %%
df_reducido = df[['nombre_com', 'diametro', 'altura_tot']].copy()

# %%
df_reducido.head()
# %%
df_reducido['nombre_com'].unique()
# %%
df_reducido['nombre_com'].value_counts()
# %%
df_jacaranda = df_reducido[df_reducido['nombre_com'] == 'Jacarandá']
df_jacaranda.describe()
# %%
# Podemos graficar directamente con Pandas...
df_jacaranda.plot.scatter(x='diametro', y='altura_tot')
# %%
# O recurrir a Seaborn
import seaborn as sns
sns.scatterplot(data=df_jacaranda, x='diametro', y='altura_tot')
# %%
cant_ejemplares = df_reducido['nombre_com'].value_counts()
#%%
# cant_ejemplares['Jacarandá'] = 'Jacaranda' # No funciona, le cambié el valor, no el index!
cant_ejemplares.head(10)
cant_ejemplares.rename(index={'Jacarandá':'Jacaranda'}, inplace=True)
