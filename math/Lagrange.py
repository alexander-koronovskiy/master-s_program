import numpy as np
import matplotlib.pyplot as plt


# lagrange interpolate with
def lagrange(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


x = np.array([1,2,3,4,5,6], dtype=float)
y = np.array([1,8,27,64,125,216], dtype=float)
xnew = np.linspace(np.min(x), np.max(x), 10)
ynew = [lagrange(x, y, i) for i in xnew]
plt.plot(x, y, 'o')
plt.plot(xnew, ynew)
plt.grid(True)
plt.show()
