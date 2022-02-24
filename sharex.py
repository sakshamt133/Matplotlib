import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([i for i in range(0, 10)])
y1 = 3 * x1 + 3

x2 = np.array([i for i in range(20, 30)])
y2 = 3 * x2 + 2

ax1 = plt.subplot2grid((2, 1), (0, 0), 1, 1)
ax1.plot(x1, y1, c='g', linewidth=3)
ax1.xaxis.set_visible(False)
plt.xlabel("X")
plt.ylabel("Y")

ax2 = plt.subplot2grid((2, 1), (1, 0), 1, 1, sharex=ax1)
ax2.plot(x1, y1, c='g', linewidth=3)
plt.xlabel("X")
plt.ylabel("Y")

plt.show()