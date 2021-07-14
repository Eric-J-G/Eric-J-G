from matplotlib import pyplot
from math import sin
import numpy as np

xs = np.arange(1, 5, 0.1)
ys = []
a = []
for x in xs:
    ys.append(sin(x))
    a.append(x)

pyplot.plot(xs, ys)
pyplot.plot(xs, a)
pyplot.show()