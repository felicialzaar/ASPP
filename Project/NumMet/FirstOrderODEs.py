"""
Numerical nethods for solving first order ordinary differential equations
on the form
                        dy/dx = f(x, y)                 (*)
                            y(0) = c                    (**)

where c is some known value.
"""

import numpy as np

def eulers_method(f, x, y0, h):
  """
  Solution of first order ODE by Eulers method.

  Parameters
  ----------
  f : function
      Right-hand side of (*).
  x : ndarray
      x-values over which to integrate the ODE.
  y0 : float
      Boundary condition (**).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  y = np.zeros(len(x))
  y[0] = y0

  for n in range(len(y) - 1):
    xn = x[n]
    yn = y[n]
    y[n + 1] = yn + h*f(xn, yn)
  return y

def taylor_expansion(f, Dfx, Dfy, x, y0, h):
  """
  Solution of first order ODE by Taylor expansion.

  Parameters
  ----------
  f : function
      Right-hand side of (*).
  Dfx : function
      Analytical derivative of (*) w.r.t. x.
  Dfy : function
      Analytical derivative of (*) w.r.t. y.
  x : ndarray
      x-values over which to integrate the ODE.
  y0 : float
      Boundary condition (**).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  y = np.zeros(len(x))
  y[0] = y0
  for n in range(len(y) - 1):
    xn = x[n]
    yn = y[n]
    fn = f(xn, yn)
    y[n + 1] = yn + (h * fn + 1/2*h**2*(Dfx(xn, yn) + Dfy(xn, yn) * fn))
  return y

def implicit_method(g, x, y0, h):
  """
  Solution of first order ODE by implicit method, where the right-hand side
  of (*) is expressed as f(x, y) = g(x)*y.

  Parameters
  ----------
  g : function
      x-dependency of right-hand side of (*).
  x : ndarray
      x-values over which to integrate the ODE.
  y0 : float
      Boundary condition (**).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  y = np.zeros(len(x))
  y[0] = y0
  for n in range(len(y) - 1):
    y[n + 1] = ((1 + h*1/2*g(x[n]))/(1 - h*1/2*g(x[n + 1])))*y[n]
  return y

def second_runge_kutta(f, x, y0, h):
  """
  Solution of first order ODE by second order Runge-Kutta.

  Parameters
  ----------
  f : function
      Right-hand side of (*).
  x : ndarray
      x-values over which to integrate the ODE.
  y0 : float
      Boundary condition (**).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  y = np.zeros(len(x))
  y[0] = y0
  for n in range(len(y) - 1):
    xn = x[n]
    yn = y[n]
    k = h*f(xn, yn)
    y[n + 1] = yn + h * f(xn + h/2, yn + k/2)
  return y

def third_runge_kutta(f, x, y0, h):
  """
  Solution of first order ODE by third order Runge-Kutta.

  Parameters
  ----------
  f : function
      Right-hand side of (*).
  x : ndarray
      x-values over which to integrate the ODE.
  y0 : float
      Boundary condition (**).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  y = np.zeros(len(x))
  y[0] = y0
  for n in range(len(y) - 1):
    xn = x[n]
    yn = y[n]
    k1 = h*f(xn, yn)
    k2 = h*f(xn + h/2, yn + k1/2)
    k3 = h*f(xn + h, yn - k1 + 2*k2)
    y[n + 1] = yn + 1/6 * (k1 + 4*k2 + k3)
  return y

def fourth_runge_kutta(f, x, y0, h):
  """
  Solution of first order ODE by fourth order Runge-Kutta.

  Parameters
  ----------
  f : function
      Right-hand side of (*).
  x : ndarray
      x-values over which to integrate the ODE.
  y0 : float
      Boundary condition (**).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  y = np.zeros(len(x))
  y[0] = y0
  for n in range(len(y) - 1):
    xn = x[n]
    yn = y[n]
    k1 = h*f(xn, yn)
    k2 = h*f(xn + h/2, yn + k1/2)
    k3 = h*f(xn + h/2, yn + k2/2)
    k4 = h * f(xn + h, yn + k3)
    y[n + 1] = yn + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
  return y
