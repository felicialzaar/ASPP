import numpy as np
import NumMet as nm
from inspect import getmembers, isfunction


def f(x): return x**2
def df(x): return 2**x
def ode(x, y): return -x*y
def g(x): return -x
def dfx(x, y): return -y
def dfy(x, y): return -x

def k(x): return -np.ones(len(x))
def S(x): return 12*x**2
def yhl(x, a=4): return 1 / np.sqrt(2 * a) * (np.exp(a * x) - np.exp(-a * x))
def yhr(x, a=4): return - 1 / np.sqrt(2 * a) * np.exp(-a * x)

for member in getmembers(nm, isfunction):
    print(member)

x = np.arange(0, 1 + 0.01, 0.01)
init = np.zeros(len(x))
#print(nm.five_point_diff(f, x, 1))
#print(nm.trapezoidal_rule(f, x, 1))
#print(nm.secant(f, -1.1, 1)[-1])
print(nm.gaussian_quadrature(f, 3))
