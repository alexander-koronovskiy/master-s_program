from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
f = interp1d(x, y)
xnew = np.linspace(0, 10, num=41, endpoint=True)

plt.plot(f(xnew))
plt.show()
