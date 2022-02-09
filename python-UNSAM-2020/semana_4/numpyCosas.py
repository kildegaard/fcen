# %%
import numpy as np

# %%
array1d = np.array([1, 2, 3, 4])
print(array1d)
print(array1d.shape)
# %%
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array2d)
print(array2d.shape)
# %%
array3d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array3d)
print(array3d.shape)
# %%
tempe = np.load('../Data/Temperaturas.npy')
tempe
