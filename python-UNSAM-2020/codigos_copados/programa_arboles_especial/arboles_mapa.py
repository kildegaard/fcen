import folium
from folium.plugins import MarkerCluster
import pandas as pd
#  cargamos el archivo a un data frame
df = pd.read_csv('Data/arbolado-en-espacios-verdes.csv')
#  creamos el mapa
mapa_arboles = folium.Map(location=[df['lat'].mean(), df['long'].mean()], zoom_start=10)
#  un cluster es una agrupacion de marcadores
cluster = MarkerCluster()
#  iteramos sobre el dataframe agregando los marcadores
for row in df.itertuples():
    row_id = str(dict(zip(df.columns, row[1:])))
    cluster.add_child(folium.Marker(location= [row.lat, row.long], popup=row_id))
#  agregamos el cluster al mapa y lo guardamos
mapa_arboles.add_child(cluster)
mapa_arboles.save('mapa_de_arboles.html')