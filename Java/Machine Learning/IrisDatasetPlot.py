import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

fig = plt.figure()
ax1 = plt.subplot(4, 3, 1)
ax2 = plt.subplot(4, 3, 2)
ax3 = plt.subplot(4, 3, 3)
ax4 = plt.subplot(4, 3, 4)
ax5 = plt.subplot(4, 3, 5)
ax6 = plt.subplot(4, 3, 6)
ax7 = plt.subplot(4, 3, 7)
ax8 = plt.subplot(4, 3, 8)
ax9 = plt.subplot(4, 3, 9)
ax10 = plt.subplot(4, 3, 10)
ax11 = plt.subplot(4, 3, 11)
ax12 = plt.subplot(4, 3, 12)


iris = load_iris()
data = np.array(iris['data'])
targets = np.array(iris['target'])

cd = {0: "r", 1: "b", 2: "g", 3: "y"}
cols = np.array([cd[target] for target in targets])

ax1.scatter(data[:, 0], data[:, 1], c=cols)
ax2.scatter(data[:, 0], data[:, 2], c=cols)
ax3.scatter(data[:, 0], data[:, 3], c=cols)
ax4.scatter(data[:, 1], data[:, 0], c=cols)
ax5.scatter(data[:, 1], data[:, 2], c=cols)
ax6.scatter(data[:, 1], data[:, 3], c=cols)
ax7.scatter(data[:, 2], data[:, 0], c=cols)
ax8.scatter(data[:, 2], data[:, 1], c=cols)
ax9.scatter(data[:, 2], data[:, 3], c=cols)
ax10.scatter(data[:, 3], data[:, 0], c=cols)
ax11.scatter(data[:, 3], data[:, 1], c=cols)
ax12.scatter(data[:, 3], data[:, 2], c=cols)

plt.show()