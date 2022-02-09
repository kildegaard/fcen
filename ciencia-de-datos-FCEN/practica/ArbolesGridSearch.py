# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:18:11 2020

@author: m_mae
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import seaborn as sn
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
#from sklearn.tree.export import export_text
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold

plt.close('all')
np.random.seed(333)
N_DATOS = 25
K = 5
split_out = int(N_DATOS / K * 4)
split = int(split_out * (K - 1) / K)
fil_graf = 2  # cantidad de filas en el subplot con los graficos
col_graf = 3  # cantidad de cols en el subplot con los graficos

low = 3   # posoción maxima en el cuadrado de datos
high = 7  # posoción minima en el cuadrado de datos

# Genreo el conjunto de datos y los pinto de dos colores
x11 = np.random.normal(high, 1, N_DATOS)
y11 = np.random.normal(high, 1, N_DATOS)
x21 = np.random.normal(low, 1, N_DATOS)
y21 = np.random.normal(high, 1, N_DATOS)
x12 = np.random.normal(low, 1, N_DATOS)
y12 = np.random.normal(low, 1, N_DATOS)
x22 = np.random.normal(high, 1, N_DATOS)
y22 = np.random.normal(low, 1, N_DATOS)

x1 = x = np.r_[x11, x12]
y1 = x = np.r_[y11, y12]
x2 = x = np.r_[x21, x22]
y2 = x = np.r_[y21, y22]
'''x1=x1-(high-low)/2
x2=x2-(high-low)/2
y1=y1-(high-low)/2
y2=y2-(high-low)/2'''
xy1 = x1 - y1
xy2 = x2 - y2

plt.figure()
plt.scatter(x1, y1, c='red')
plt.scatter(x2, y2, c='blue')
plt.xlabel('Planificado 100k usd')
plt.ylabel('Ejecutadoado 100k usd')
plt.legend(['Éxitos', 'Fracasos'])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, xy1, c='red')
ax.scatter(x2, y2, xy2, c='blue')
plt.xlabel('Planificado 100k usd')
plt.ylabel('Ejecutadoado 100k usd')
ax.set_zlabel('Diferencia 100k usd')
plt.legend(['Éxitos', 'Fracasos'])

plt.figure()
plt.scatter(x1, xy1, c='red')
plt.scatter(x2, xy2, c='blue')
plt.xlabel('Planificado 100k usd')
plt.ylabel('Diferencia 100k usd')
plt.legend(['Éxitos', 'Fracasos'])
# apilo los x correspondentes a las dos clases
x = np.r_[x1, x2]
# lo paso a forma de un vector de una columna
x = x.reshape(-1, 1)
# idem ocn Y
y = np.r_[y1, y2]
y = y.reshape(-1, 1)

xy = x - y

z = np.r_[np.zeros((2 * N_DATOS, 1)), np.ones((2 * N_DATOS, 1))]
# crero un nuevo x con las columnas de x e y
t = np.c_[x, y, xy, z]


df = pd.DataFrame(t, columns=['x', 'y', 'xy', 'z'])
df = df.sample(frac=1).reset_index(drop=True)

p_grid = {"max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

# Creo el objeto pls
#pls = PLSRegression()


tree2 = DecisionTreeClassifier(min_samples_leaf=3)


# Preparo los splits para corsvalidar
inner_cv = KFold(n_splits=4, shuffle=False)

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=tree2, param_grid=p_grid, cv=inner_cv, scoring='accuracy')  # neg_root_mean_squared_error')
x_train = df[['x', 'xy']]
z_train = df['z']
clf.fit(x_train, z_train)

# posic=clf.cv_results_['rank_test_score'][5]
#profposta = p_grid['max_depth'][posic-1]
profposta = 4
print('Profundidad optima: ', profposta)

treeoptimo = DecisionTreeClassifier(max_depth=profposta, min_samples_leaf=3)
treeoptimo.fit(x_train, z_train)

#error_medio_cvs= -clf.best_score_


plt.figure()
tree.plot_tree(treeoptimo, filled=True)
#tree.plot_tree(clf, filled=True)
#plot_tree(clf, filled=True)
# plt.show()


# Elijo con el mejor modelo
# posic=clf.cv_results_['rank_test_score'][0]
#posta = p_grid['n_components'][posic-1]
#print('Número de componentes: ',posta)
