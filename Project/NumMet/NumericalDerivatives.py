"""
Numerical nethods for first derivatives of 1D functions. Includes three-point,
five-point, foward and backward difference formulas.
"""

import numpy as np

def three_point_diff(f, x, h):
  """
  Three-point difference formula. Ordo h^2.

  Parameters
  ----------
  f : function
      Function at which to take derivatve.
  x : ndarray, float, or int
      Point(s) at which to evaluate derivative.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  ndarray, float, or int
      Numerical derivative at points x.
  """

  return (f(x + h) - f(x - h))/ (2 * h)

def forward_diff(f, x, h):
  """
  Forward difference formula. Ordo h.

  Parameters
  ----------
  f : function
      Function at which to take derivatve.
  x : ndarray, float, or int
      Point(s) at which to evaluate derivative.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  ndarray, float, or int
      Numerical derivative at points x.
  """

  return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
  """
  Forward difference formula. Ordo h.

  Parameters
  ----------
  f : function
      Function at which to take derivatve.
  x : ndarray, float, or int
      Point(s) at which to evaluate derivative.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  ndarray, float, or int
      Numerical derivative at points x.
  """

  return (f(x) - f(x - h)) / h

def five_point_diff(f, x, h):
  """
  Three-point difference formula. Ordo h^4.

  Parameters
  ----------
  f : function
      Function at which to take derivatve.
  x : ndarray, float, or int
      Point(s) at which to evaluate derivative.
  h : float
      Step size, i.e. distance between points in x.

  Returns
  -------
  ndarray, float, or int
      Numerical derivative at points x.
  """
  return 1/(12*h)*(f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h))
