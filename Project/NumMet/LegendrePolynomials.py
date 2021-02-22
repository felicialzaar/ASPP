"""
Numerical Legendre polynomials and their roots.
"""

import numpy as np

def legendre_polynomial(l, x):
  """
  Legandre polynomial at points x.

  Parameters
  ----------
  l : int
      Index of Legendre polynomial.
  x : ndarray
      Points at which to evaluate Legendre polynomial l.

  Returns
  -------
  ndarray
      Legandre polynomial l at points x.
  """

  if isinstance(x, (np.floating, float, int)):
    x = np.array([x])

  if l == 0:
    return np.ones(len(x))
  elif l == 1:
    return x
  else:
    return (((2 * l)-1)*x * legendre_polynomial(l-1, x)-(l-1)*legendre_polynomial(l-2, x))/float(l)

def legendre_derivative(l, x):
  """
  Derivative of Legandre polynomial l at points x.

  Parameters
  ----------
  l : int
      Index of Legendre polynomial.
  x : ndarray
      Points at which to evaluate Legendre polynomial l.

  Returns
  -------
  ndarray
      Derivative of Legandre polynomial l at points x.
  """

  if isinstance(x, (np.floating, float, int)):
    x = np.array([x])

  if l == 0:
    return np.zeros(len(x))
  elif l == 1:
    return np.ones(len(x))
  else:
    return (-l * x * legendre_polynomial(l, x) + l * legendre_polynomial(l - 1, x)) / (1 - x ** 2)

def legendre_roots(l, tol=1e-10):
  """
  Finds all roots of Legandre polynomial l.

  Parameters
  ----------
  l : int
      Index of Legendre polynomial.
  tol : float, optional
      Tolerance of difference between numerical and true root.

  Returns
  -------
  ndarray
      All roots of Legendre polynomial l.
  """

  def bisection_method(an, bn, l, f, tol):
    """
    Finds a single root of Legandre polynomial l.

    Parameters
    ----------
    an : float
         Lower search limit.
    bn : float
         Upper search limit.
    l : int
        Index of Legandre polynomial
    tol: float
         Tolerance of difference between numerical and true root.

    Returns
    -------
    float
        Single root of Legendre polynomial l.
    """

    fa = f(l, an)

    if fa * f(l, bn) > 0:
      return None

    cn = (an + bn) / 2
    fc = f(l, cn)
    condition = True
    while condition:
      if  fa * fc  < 0:
        bn = cn
      else:
        an = cn
      fa = f(l, an)
      cn = (an + bn) / 2
      fc = f(l, cn)
      condition = np.abs(fc) > tol

    return np.round(cn, int(abs(np.log10(tol))) - 1)

  a = -1
  b = 1
  xn = (b - a) / (l * 4)

  all_roots = []
  while a < b - xn:
    root = bisection_method(a, a + xn, l, legendre_polynomial, tol)
    if root not in all_roots and root is not None:
      all_roots.append(root)
    a += xn

  return np.asarray(all_roots)
