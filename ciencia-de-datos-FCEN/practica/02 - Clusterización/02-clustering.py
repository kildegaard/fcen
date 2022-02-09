
"""
Created on Sat Nov 14 16:15:27 2020

@author: gus
"""
# %%
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# plt.style.use('seaborn-poster')
plt.xkcd()

(x1, y1) = (5, 5)
(x2, y2) = (20, 5)
(x3, y3) = (15, 20)

np.random.seed(1337)

X1 = np.random.normal(x1, 3, 50)
Y1 = np.random.normal(y1, 3, 50)

X2 = np.random.normal(x2, 3, 50)
Y2 = np.random.normal(y2, 3, 50)

X3 = np.random.normal(x3, 3, 50)
Y3 = np.random.normal(y3, 3, 50)

####
# %%
fig, ax = plt.subplots()

ax.set_title('Puntos al azar')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True, zorder=0)

ax.scatter(X1, Y1,
           marker='o',
           facecolor='red',
           edgecolor='black',
           zorder=3,
           label='Grupo 1')

ax.scatter(X2, Y2,
           marker='o',
           facecolor='green',
           edgecolor='black',
           zorder=3,
           label='Grupo 2')

ax.scatter(X3, Y3,
           marker='o',
           facecolor='blue',
           edgecolor='black',
           zorder=3,
           label='Grupo 3')


ax.legend(loc='upper left')

# %%
# Armar una matriz con los datos

X1 = X1.reshape(len(X1), 1)
Y1 = Y1.reshape(len(Y1), 1)

X2 = X2.reshape(len(X2), 1)
Y2 = Y2.reshape(len(Y2), 1)

X3 = X3.reshape(len(X3), 1)
Y3 = Y3.reshape(len(Y3), 1)

X = np.concatenate((X1, X2, X3), axis=0)
Y = np.concatenate((Y1, Y2, Y3), axis=0)
mat = np.c_[X, Y]

# %%
Sum_of_squared_distances = []
K = range(1, 7)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(mat)
    Sum_of_squared_distances.append(km.inertia_)

plt.figure()
plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

# %%
# La parte del KMeans


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 8), sharey=True)

km = KMeans(n_clusters=2)
km_fit1 = km.fit(mat)
ax[0].scatter(X, Y,
              c=km_fit1.labels_,
              cmap='plasma',
              marker='o',
              edgecolor='black')
ax[0].set_title('Usando 2 clústers')

km = KMeans(n_clusters=3, random_state=0)
km_fit2 = km.fit(mat)
ax[1].scatter(X, Y,
              c=km_fit2.labels_,
              cmap='plasma',
              marker='o',
              edgecolor='black')
ax[1].set_title('Usando 3 clústers')

# %%

T = km_fit1.labels_

mT = T.reshape(10, 15, order='F')

plt.figure()
plt.imshow(mT)
