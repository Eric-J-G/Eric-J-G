from matplotlib import pyplot
from math import cos
import numpy as np

xs = np.arange(-10, 10, 0.1)
ys = []
a = []
for x in xs:
    ys.append(x ** 2 - 30)
    a.append(2*x + 1)
pyplot.plot(xs, ys)
pyplot.plot(xs, a)
pyplot.show()