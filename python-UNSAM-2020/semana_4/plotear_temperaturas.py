import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('../Data/Temperaturas.npy')

plt.hist(temperaturas, bins=50)
plt.show()
