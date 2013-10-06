#!/usr/bin/env python

import numpy as np


def params(M):
    return np.vstack([row[1] for row in M])

def coeffs(M):
    return [row[0] for row in M]

def reduce_row(M):
    """
    >>> C = [84, 96, 72]
    >>> M = [list(row) for row in zip(np.array(C), np.identity(len(C)))]
    >>> reduce_row(M)
    [[72, array([ 0.,  0.,  1.])], [84, array([ 1.,  0.,  0.])], [24, array([ 0.,  1., -1.])]]
    """
    M_n = sorted(filter(lambda row: row[0] != 0, M), key=lambda el: el[0])
    if len(M_n) == 1:
        print 'Nothing to solve for!'
        return M
    d, m = divmod(M_n[-1][0], M_n[0][0])
    M_n[-1][0] = m
    M_n[-1][1] -= d * M_n[0][1]
    return filter(lambda row: row[0] == 0, M) + filter(lambda row: row[0] !=0, M_n)

def solve_dioph_eqn(C):
    """
    >>> solve_dioph_eqn([84, 96, 72])
    ([0, 0, 12], array([[ -6.,  18., -17.],
           [ -2.,   7.,  -7.],
           [  1.,  -3.,   3.]]))
    """
    M = [list(row) for row in zip(np.array(C), np.identity(len(C)))]
    while coeffs(M).count(0) < len(M)-1:
        M = reduce_row(M)
        # print M
        # print
    return (coeffs(M), params(M))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print solve_dioph_eqn([84, 96, 72])
