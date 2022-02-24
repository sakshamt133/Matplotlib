import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    ax.clear()
    df = pd.read_csv("live_data.csv")
    x = df['x']
    y = df['y']
    ax.plot(x, y, c='b', linewidth=5)
    plt.xlabel("X")
    plt.ylabel("Y")


ani = animation.FuncAnimation(fig, animate, 1000)
plt.show()

