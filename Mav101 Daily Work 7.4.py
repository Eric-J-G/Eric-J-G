from matplotlib import pyplot
from math import cos
import numpy as np

xs = np.arange(0, 30, 0.1)
ys = []

for x in xs:
    ys.append(cos(x))

pyplot.plot(xs, ys)
pyplot.show()