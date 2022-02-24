import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([i for i in range(0, 10)])
y1 = 3 * x1 + 3

plt.fill_between(x1, y1, 15, where=(y1 < 15), alpha=0.2, facecolor='g')
plt.show()
