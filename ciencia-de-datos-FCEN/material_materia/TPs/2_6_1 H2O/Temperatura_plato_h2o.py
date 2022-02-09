# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:22:40 2020

@author: Y149681
"""
#h2o.cluster().shutdown(prompt=True) 
import h2o
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from h2o.automl import H2OAutoML

h2o.init()

#df = pd.read_csv('U300_web_7_9_2017.csv')
df = h2o.import_file('U300_web_7_9_2017.csv')
#descrip = df.describe()

df = df.drop([0,1])


# churn_df = h2o.import_file('https://raw.githubusercontent.com/srivatsan88/YouTubeLI/master/dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df_py = h2o.as_list(df)
df_py = df_py.iloc[::2,:]
df = h2o.H2OFrame(df_py)
filast= df_py.shape[0]


n_train = df[:np.floor(filast*.8),:]
n_train_py = h2o.as_list(n_train)
filas = n_train_py.shape[0]

filas_fold = np.ones((np.int(filas/5),1))
fold = filas_fold
for i in range(1,4):
    fold = np.r_[fold,filas_fold*(i+1)]
fold = np.r_[fold,5*np.ones((filas-np.int(filas/5)*4,1))]
df_fold = pd.DataFrame(data=fold, columns=["fold"])


fold_numbers = h2o.H2OFrame(df_fold)
n_train = n_train.cbind(fold_numbers)
n_train_py = h2o.as_list(n_train)

#n_valid = df[np.floor(filas*.6)+1:np.floor(filas*.8),:]
n_test = df[np.floor(filast*.8)+1:,:]

#n_train,n_test,n_valid = df.split_frame(ratios=[.7, .15])

n_test_py = h2o.as_list(n_test)
#n_valid_py = h2o.as_list(n_valid)


y = n_train_py.columns[27]
x = df.columns
x.remove(y)
# x.remove("customerID")

aml = H2OAutoML(max_models = 20, seed = 10, exclude_algos = ["DeepLearning"], verbosity="info", nfolds=5)
aml.train(x = x, y = y, training_frame = n_train,fold_column="fold")
#cars_gbm.train(x=predictors, y=response, training_frame=cars, fold_column="fold_numbers")

lb = aml.leaderboard
lb_py = h2o.as_list(lb)
print(lb.head)


n_pred=aml.leader.predict(n_test)
n_pred_py = h2o.as_list(n_pred)
y_test_py = n_test_py[y]

plt.figure()
plt.scatter(y_test_py,n_pred_py)

# grabo modelo
modelo = aml.leader
n_pred=modelo.predict(n_test)
modelo_guardado = h2o.save_model(model=modelo,path="/tmp/mymodel", force=True)
print (modelo_guardado)


# load the model
modelo2 = h2o.load_model(modelo_guardado)
n_pred2=modelo2.predict(n_test)




