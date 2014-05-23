#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

data_fname = 'knot_points.csv'

def read_data(fname):
    X = []
    Y = []
    with open(fname, 'r') as f:
        for line in f:
            (x, y) = line.split(',')
            X.append(float(x))
            Y.append(float(y))
    return (X, Y)

def lagrange_polynomial(X, Y):
    def L(i):
        return lambda x: np.prod([(x-X[j])/(X[i]-X[j]) for j in range(len(X)) if i != j]) * Y[i]
    Sx = [L(i) for i in range(len(X))]  # summands
    return lambda x: np.sum([s(x) for s in Sx])

# F = lagrange_polynomial(*read_data(data_fname))
(X, Y) = read_data(data_fname)
x_range = np.linspace(X[0], X[-1], 100)
F = lagrange_polynomial(X, Y)

plt.plot(X, Y, 'ro')
plt.plot(x_range, map(F, x_range))
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.title('Lagrange polynomial interpolation')
plt.grid(True)
# plt.savefig('plot.png')
plt.show()
