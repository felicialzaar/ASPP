"""
Numerical nethods for findinf roots of 1D functions.
"""

import numpy as np

def search(f, x0, h0, tol=1e-10):
  """
  Search algorithm for single root. Add decreasing increment h to inital guess
  smaller than true root, until h is smaller than tolerance.

  Parameters
  ----------
  f : function
      Function for which to find a single root.
  x0 : float
      Initial guess. Must be smaller than true root.
  h0 : float
      Initial increment.
  tol : float, optional
      Tolerance of difference between numerical and true root. Default is 1e-10.

  Returns
  -------
  all_iter : ndarray
      Root at each iteration.
  """

  xi = x0

  all_iter = [x0]
  while h0 >= tol:
    if np.sign(f(xi + h0)) != np.sign(f(x0)):
      xi = xi - h0
      h0 = h0 / 2
    xi = xi + h0
    all_iter.append(xi)
  return np.array(all_iter)

def newton_raphson(f, Df, x0, tol=1e-10):
  """
  Newton-Raphson method.

  Parameters
  ----------
  f : function
      Function for which to find a single root.
  Df : function
      Analytical derivative of function. Cannot be 0 anywhere.
  x0 : float
      Initial guess. Must be larger than true root.
  tol : float, optional
      Tolerance of difference between  f(xi) and 0.

  Returns
  -------
  all_iter : ndarray
      Root at each iteration.
  """

  xi = x0
  yi = f(xi)
  dyi = Df(xi)

  all_iter = [x0]
  while abs(yi) >= tol:
    xi = xi - yi/dyi
    yi = f(xi)
    dyi = Df(xi)
    all_iter.append(xi)
  return np.array(all_iter)

def secant(f, x0, x1, tol=1e-10):
  """
  Newton-Raphson method.

  Parameters
  ----------
  f : function
      Function for which to find a single root.
  x0 : float
      Left initial guess. Must be smaller than true root.
  x1 : float
      Right initial guess. Must be larger than true root.
  tol : float, optional
      Tolerance of difference between numerical and true root. Default is 1e-10.

  Returns
  -------
  all_iter : ndarray
      Root at each iteration.
  """

  x_left = x0
  x_right = x1
  y_left = f(x_left)
  y_right = f(x_right)

  all_iter = [x_right]
  while np.abs(x_right - x_left) >= tol:
    x_new = x_right - y_right * (x_right - x_left)/(y_right - y_left)
    x_left = x_right
    x_right = x_new
    y_left = f(x_left)
    y_right = f(x_right)
    all_iter.append(x_new)
  return np.array(all_iter)
