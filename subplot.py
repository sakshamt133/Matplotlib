import matplotlib.pyplot as plt
import numpy as np

# Method 1
x1 = np.array([i for i in range(0, 10)])
y1 = 3 * x1 + 3

x2 = np.array([i for i in range(20, 30)])
y2 = 3 * x2 + 2

ax1 = plt.subplot2grid((1, 2), (0, 0), 1, 1)
ax1.plot(x1, y1, c='g', linewidth=3)
plt.xlabel("X")
plt.ylabel("Y")

ax2 = plt.subplot2grid((1, 2), (0, 1), 1, 1)
ax2.plot(x2, y2, c='b')
plt.show()

# Method 2
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x1, y1)
plt.show()