"""
Numerical nethods for integration of 1D functions. Includes trapezoidal, Bode
and Simpson formulas.
"""

import numpy as np
from .LegendrePolynomials import legendre_roots, legendre_derivative

def trapezoidal_rule(f, x, h):
  """
  Trapezoidal rule. Ordo h^3.

  Parameters
  ----------
  f : function
      Function to integrate.
  x : ndarray
      Points over which to evaluate integral.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  float
      Numerical integral over points x.
  """

  y_left = y[:-2][::2]
  y_center = y[1:-1][::2]
  y_right = y[2:][::2]
  return h/2 * sum(y_left + 2*y_center + y_right)

def simpsons_rule(f, x, h):
  """
  Simpson's rule. Ordo h^5.

  Parameters
  ----------
  f : function
      Function to integrate.
  x : ndarray
      Points over which to evaluate integral.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  float
      Numerical integral over points x.
  """

  y = f(x)
  y_left = y[:-2][::2]
  y_center = y[1:-1][::2]
  y_right = y[2:][::2]
  return h/3 * sum(y_left + 4*y_center + y_right)

def bodes_rule(f, x, h):
  """
  Bode's rule. Ordo h^7.

  Parameters
  ----------
  f : function
      Function to integrate.
  x : ndarray
      Points over which to evaluate integral.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  float
      Numerical integral over points x.
  """

  y = f(x)
  y0 = y[:-4][::4]
  y1 = y[1:-3][::4]
  y2 = y[2:-2][::4]
  y3 = y[3:-1][::4]
  y4 = y[4:][::4]

  return (2*h/45) * sum(7*y0 + 32*y1 + 12*y2 + 32*y3 + 7*y4 )

def gaussian_quadrature(func, l, tol=1e-10):
  """
  Gaussian quadrature with Legendre polynomials.

  Parameters
  ----------
  f : function
      Function to integrate.
  l : int
      Index of Legendre polynomial to use for abscissae, i.e. number of roots.
  tol: float
      Tolerance of difference between numerical and true root.

  Returns
  -------
  float
      Numerical integral over points x.
  """

  roots = legendre_roots(l, tol)
  weights = 2/((1 - roots**2) * legendre_derivative(l, roots)**2)
  return sum(weights * func(roots))
