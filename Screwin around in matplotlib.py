import numpy
from matplotlib import pyplot
xs = numpy.linspace(-10, 10, 50)
ys = []
for x in xs:
    ys.append(x ** 2)

pyplot.plot(xs, ys)
pyplot.show()