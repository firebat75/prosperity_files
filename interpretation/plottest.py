import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3)
x = np.array([11, 12, 13, 14, 15])
y = np.array([1, 2, 3, 4, 5])
print(x)
print(y)
# size and color:
# sizes = np.random.uniform(15, 80, len(x))
# colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

# ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
ax.scatter(x, y)

# ax.set(xlim=(8, 15), xticks=np.arange(8, 15),
#        ylim=(8, 15), yticks=np.arange(8, 15))

plt.show()
