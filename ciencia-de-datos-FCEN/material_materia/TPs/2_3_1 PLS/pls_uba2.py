# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:23:06 2020

@author: Y149681
"""

from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
import numpy as np
from sklearn.cross_decomposition import PLSRegression
import pandas as pd

plt.close('all')
'''
 pls2 = PLSRegression(n_components=2)
>>> pls2.fit(X, Y)
PLSRegression(algorithm='nipals', copy=True, max_iter=500, n_components=2,
       scale=True, tol=1e-06)
>>> Y_pred = pls2.predict(X)
'''
# Number of random trials
NUM_TRIALS = 1

# Load the dataset
df = pd.read_csv('U300_web_7_9_2017.csv')
# df=df.iloc[:-1000,:]
#df=df.drop(df.iloc[:, 50:51], axis = 1)
Xi = df.iloc[:-1000, 2:-1]
Xitest = df.iloc[-1000:, 2:-1]
Xg = Xi.drop(Xi.columns[26:27], axis=1)
Xtest = Xitest.drop(Xitest.columns[26:27], axis=1)
Yg = df.iloc[:-1000, 26:27]
Ytest = df.iloc[-1000:, 26:27]

'''for i, col in enumerate(Xg.columns):
    df[col].plot(fig=plt.figure(i))
    plt.title(col)'''

# Set up possible values of parameters to optimize over
p_grid = {"n_components": [10, 11, 12, 13, 14, 15, 16, 17]}

# We will use a Support Vector Classifier with "rbf" kernel
pls = PLSRegression()

# Arrays to store scores
#non_nested_scores = np.zeros(NUM_TRIALS)
#nested_scores = np.zeros(NUM_TRIALS)

# Loop for each trial

# Choose cross-validation techniques for the inner and outer loops,
# independently of the dataset.
# E.g "GroupKFold", "LeaveOneOut", "LeaveOneGroupOut", etc.
inner_cv = KFold(n_splits=4, shuffle=False)
outer_cv = KFold(n_splits=4, shuffle=False)

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=pls, param_grid=p_grid, cv=inner_cv, scoring='neg_root_mean_squared_error')
clf.fit(Xg, Yg)
error_medio_cvs = -clf.best_score_

# Nested CV with parameter optimization
nested_score = cross_val_score(clf, X=Xg, y=Yg, cv=outer_cv, scoring='neg_root_mean_squared_error')
error_medio_nested = -nested_score.mean()
#print( 'test: ',test,'     score: ',nested_score.mean())


# entreno con el mejor modelo
posic = clf.cv_results_['rank_test_score'][0]
posta = p_grid['n_components'][posic - 1]
print('Número de componentes: ', posta)

pls = PLSRegression(n_components=posta)
pls.fit(Xg, Yg)
Yp = pls.predict(Xtest)
plt.figure()
plt.scatter(Yp, Ytest)
plt.xlabel('Estimado')
plt.ylabel('Medido')
error_medio_medido = np.sqrt(np.sum(np.square(Ytest.to_numpy() - Yp)) / np.shape(Yp)[0])

plt.figure()
plt.plot(Ytest.to_numpy())
plt.plot(Yp)
plt.title('Trends para predicho y medido')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura')

print("Error CV: {:6f} - Error nested: {:6f} Error medido: {:6f}".format(error_medio_cvs, error_medio_nested, error_medio_medido))
