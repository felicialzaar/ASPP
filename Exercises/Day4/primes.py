import numpy
"""
Calculates forst kmax primes
"""

def primes(kmax):
    p = numpy.zeros((1000), dtype=numpy.int)
    results = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    k = 2
    while k < kmax:
        i = 0
        while i < k and n%p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = k + 1
            result.append(n)
        n = n + 1
    return result
