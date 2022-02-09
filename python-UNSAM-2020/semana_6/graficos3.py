import matplotlib.pyplot as plt
import numpy as np

figura_1 = plt.figure(num=1, figsize=(10, 6), dpi=80, facecolor='grey', edgecolor='cyan', frameon=True)


plt.subplot(2, 1, 1)
plt.plot([0, 1, 2], [0, 1, 0])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4)
plt.plot([1, 2, 3], [1, 2, 3])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5)
plt.plot([1, 2, 3], [1, 1, 1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6)
plt.plot([1, 2, 3], [3, 2, 1])
plt.xticks([]), plt.yticks([])

plt.show()
