import matplotlib.pyplot as plt
import numpy as np

# Draw a line
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = 2 * x1 + 3

plt.plot(x1, y1, c='r')
plt.legend('Red Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# Scatter the plot
plt.scatter(x1, y1, c='b', marker='*')
plt.show()