import os
#%%
for root, dirs, files in os.walk(os.path.join('C:\\', 'Rmnt bckp')):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
#%%
directorio = os.path.join('C:\\', 'Rmnt bckp')
os.chdir(directorio)
os.mkdir('probando')
print(os.listdir('.'))
os.rmdir('probando')
print(os.listdir('.'))