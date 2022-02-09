# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:26:24 2019

@author: Y149681
"""
from sklearn.tree._export import plot_tree
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
from sklearn.tree.export import export_text
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')
np.random.seed(333)
N_DATOS=25
K=5
split_out=int(N_DATOS/K*4)
split=int(split_out*(K-1)/K)
fil_graf=2 #cantidad de filas en el subplot con los graficos
col_graf=3 #cantidad de cols en el subplot con los graficos

low=3   # posoción maxima en el cuadrado de datos
high=7  # posoción minima en el cuadrado de datos

#Genreo el conjunto de datos y los pinto de dos colores
x11 = np.random.normal(high, 1, N_DATOS)
y11 = np.random.normal(high,1, N_DATOS)
x21 = np.random.normal(low, 1, N_DATOS)
y21 = np.random.normal(high, 1, N_DATOS)
x12 = np.random.normal(low, 1, N_DATOS)
y12 = np.random.normal(low, 1, N_DATOS)
x22 = np.random.normal(high, 1, N_DATOS)
y22 = np.random.normal(low, 1, N_DATOS)

x1=x=np.r_[x11,x12]
y1=x=np.r_[y11,y12]
x2=x=np.r_[x21,x22]
y2=x=np.r_[y21,y22]
'''x1=x1-(high-low)/2
x2=x2-(high-low)/2
y1=y1-(high-low)/2
y2=y2-(high-low)/2'''
xy1=x1-y1
xy2=x2-y2

plt.figure()
plt.scatter(x1,y1,c='red')
plt.scatter(x2, y2,c='blue')
plt.xlabel('Planificado 100k usd')
plt.ylabel('Ejecutadoado 100k usd')
plt.legend(['Éxitos','Fracasos'])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, xy1,c='red')
ax.scatter(x2, y2, xy2,c='blue')
plt.xlabel('Planificado 100k usd')
plt.ylabel('Ejecutadoado 100k usd')
ax.set_zlabel('Diferencia 100k usd')
plt.legend(['Éxitos','Fracasos'])

plt.figure()
plt.scatter(x1,xy1,c='red')
plt.scatter(x2, xy2,c='blue')
plt.xlabel('Planificado 100k usd')
plt.ylabel('Diferencia 100k usd')
plt.legend(['Éxitos','Fracasos'])
#apilo los x correspondentes a las dos clases
x=np.r_[x1,x2]
#lo paso a forma de un vector de una columna
x=x.reshape(-1,1)
# idem ocn Y
y=np.r_[y1,y2]
y=y.reshape(-1,1)

xy=x-y

z=np.r_[np.zeros((2*N_DATOS,1)),np.ones((2*N_DATOS,1))]
#crero un nuevo x con las columnas de x e y
t=np.c_[x,y,xy,z]



df=pd.DataFrame(t,columns=['x','y','xy','z'])
df = df.sample(frac=1).reset_index(drop=True)



#separo training de testing
#fig, axes = plt.subplots(nrows=5, ncols=2)

contador = 0
resultados_out=pd.DataFrame(columns=['profundidad','score'])
for outer in range(K):
    df2=df
    df_test=df2.iloc[(outer)*split:(outer+1)*split,:]
    tiro=df2.iloc[(outer)*split:(outer+1)*split,:].index
    df2=df2.drop(tiro)
    x_test_out=df_test[['x','xy']]
    z_test_out=df_test[['z']]

    resultados=pd.DataFrame(columns=['profundidad','split','score'])
    resul_prof=pd.DataFrame(columns=['profundidad','score'])
    for prof in range(1,11):
        contador=0
        resul_prof=resul_prof.append({'profundidad':prof,'score':0},ignore_index=True)
        #fig, ax = plt.subplots(fil_graf, col_graf)
        for fil in range(fil_graf):
            for col in range(col_graf):
                contador = contador + 1
                if contador == K+1:
                    break 
                #selecciono mi split
                x_train=df2[['x','xy']]
                z_train=df2['z']
                x_test=x_train.iloc[(contador-1)*split:(contador)*split,:]
                z_test=z_train.iloc[(contador-1)*split:(contador)*split]
                tiro=x_train.iloc[(contador-1)*split:(contador)*split,:].index
                x_train=x_train.drop(tiro)
                z_train=z_train.drop(tiro)
                clf = DecisionTreeClassifier(max_depth=prof,min_samples_leaf=3)
                clf.fit(x_train, z_train)
               
                sc=clf.score(x_test,z_test)
                resultados=resultados.append({'profundidad':prof,'split':contador,'score':sc}, ignore_index=True)
                #ax[fil,col].set_title(sc)
                resul_prof['score'].iloc[-1]=resul_prof['score'].iloc[-1]+sc/K
                #ax.set_title(sc)
    best = resul_prof[resul_prof['score']==resul_prof['score'].max()].index.values.astype(int)[0]
    best_prof=resul_prof['profundidad'][best]
    clf = DecisionTreeClassifier(max_depth=best_prof,min_samples_leaf=3)
    clf.fit(df2[['x','xy']], df2['z'])
    plt.figure()
    xx, xxyy = np.meshgrid(np.arange(-1, 10, .05),np.arange(-7, 7, .05))
    Z = clf.predict(np.c_[xx.ravel(), xxyy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, xxyy, Z, cmap=plt.cm.RdYlBu) 
    plt.scatter(df['x'][df['z']==1], df['xy'][df['z']==1],s=20,c='red')
    plt.scatter(df['x'][df['z']==0], df['xy'][df['z']==0],s=20,c='blue')
    plt.scatter(df2['x'], df2['xy'],s=20,c='black', marker='x')
    plt.xlabel('Palnificado')
    plt.ylabel('Diferencia')
    sc=clf.score(x_test_out,z_test_out)
    plt.title('Profundidad: ' + str(best_prof) + '    Score: ' + str(sc))
    
    resultados_out=resultados_out.append({'profundidad':best_prof,'score':sc}, ignore_index=True)
    plt.figure()
    plot_tree(clf, filled=True)
    plt.show()
    #plt.title('Profndidad: ' + str(best_prof) + '    Score: ' + str(sc))

