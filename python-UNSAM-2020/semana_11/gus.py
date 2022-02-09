x = [i for i in range(10)]
y1 = [h**2 for h in x]
print(x)

import matplotlib.pyplot as plt

y = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

plt.plot(x, y, color='red')
plt.plot(x, y1, color='green')
plt.show()
