import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

plt.xlim(-2 * np.pi, 2 * np.pi)
plt.xticks([])
plt.ylim(-2 * np.pi, 2 * np.pi)
plt.yticks([])

plt.figure(1)
T = np.arctan2(Y, X)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)


plt.figure(2)
T = np.arctan2(X, Y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)


plt.show()
