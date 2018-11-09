import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 201)
y1 = np.sqrt(1-x**2)
y2 = - np.sqrt(1-x**2)

plt.plot(x, y1, color='k')
plt.plot(x, y2, color='k')
plt.axes().set_aspect('equal')

plt.savefig('circle.png')


