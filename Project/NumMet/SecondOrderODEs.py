"""
Numerical methods for solving second order ordinary differential differential
equations on the form

                    d^y/dx^2 + k^2(x)y = S(x)           (*)
                    y(0) = c1,  y(h) = c2               (**)

where S(x) is the source.
"""

import numpy as np

def numerov_algorithm(x, k, S, init, h, linear_correction=False):
  """
  Solution of inhomogeneous second order ODE by the Numerov algorithm. Linear
  correction optional.

  Parameters
  ----------
  x : ndarray
      x-values over which to integrate the ODE.
  k : function
      k(x) in (*).
  S : function
      Source term S(x) in (*).
  init : array_like
      Initial conditions y(x = 0) and y(x = h) (**).
  h : float
      Step size, i.e. distance between x-values.
  linear_correction : bool, optional
      Subtraction of linear correction if wrong behavior at large x. Default is
      False.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x, with optionally subtracted
      linear correction.
  """

  def correction(y_old, xx):
    """
    Linear correction if wrong behavior at large x.

    Parameters
    ----------
    y_old : ndarray
         Result of Numerov algrorithm without correction.
    xx : ndarray
         x-values where y has been evaluated.

    Returns
    -------
    ndarray
        Approximation of y(x) after linear correction.
    """

    k = (y[-1] - y[-10])/(x[-1] - x[-10])
    return y_old - k * x

  y = np.zeros(len(x))
  y[0] = init[0]
  y[1] = init[1]
  Sn = S(x)
  kn = k(x)
  c1 = h**2/12
  for n in range(1, len(y) - 1):
    y[n + 1] = (2*(1 - 5*c1*kn[n]**2)*y[n] - (1 + c1* kn[n - 1]**2)*y[n - 1]
                + c1 * (Sn[n + 1] + 10*Sn[n] + Sn[n - 1]))/(1 + c1*kn[n + 1]**2)

  return correction(y, x) if linear_correction else y


def greens_method(x, yh_left, yh_right, S, h):
  """
  Solution of inhomogeneous second order ODE by using a Green's function
  G(x, x') = yh_left(x) * yh_right(x).

  Parameters
  ----------
  x : ndarray
      x-values over which to integrate the ODE. Must have len(x)%4 == 0
  yh_left : function
      Homogeneous solution for x < x'.
  yh_right : function
      Homogeneous solution for x > x'.
  S : function
      Source term S(x) in (*).
  h : float
      Step size, i.e. distance between x-values.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  def bodes_rule(x, yh, S, h):
    """
    Integrates according to Bode's rule. Returns accumulated sum of integral
    at each x-value.

    Parameters
    ----------
    x : ndarray
        x-values over which to integrate the ODE. Must have len(x)%4 == 0
    yh: function
        Homogeneous solution for either x < x' or x > x'.
    S : function
        Source term S(x) in (*).
    h : float
        Step size, i.e. distance between x-values.

    """

    y = yh(x) * S(x)
    y0 = y[:-4][::4]
    y1 = y[1:-3][::4]
    y2 = y[2:-2][::4]
    y3 = y[3:-1][::4]
    y4 = y[4:][::4]

    return np.cumsum((2 * h / 45) * (7 * y0 + 32 * y1 + 12 * y2 + 32 * y3 + 7 * y4))

  I1 = bodes_rule(x, yh_left, S, h)
  I2 = bodes_rule(x, yh_right, S, h)
  I2 = I2[-1] - I2 # When I1 is integrated over small interval, I2 is integrated over rest.

  x_steps = x[::4][-1]
  return yh_right(x_steps) * I1 + yh_left(x_steps) * I2


def variational_method(x, S, init, omega, h, n_sweeps, n_interpolations=0):
  """
  Solution of inhomogeneous second order ODE by using variational principle.

  Parameters
  ----------
  x : ndarray
      x-values over which to integrate the ODE. Must have len(x)%4 == 0
  S : function
      Source term S(x) in (*).
  init: ndarray
      Initial values at all x.
  omega : float
      Convergence condition. Must be between 0 and 2.
  h : float
      Step size, i.e. distance between x-values.
  n_sweeps : int
      Number of lattice sweeps.
  n_interpolations : int, optional
      If larger than zero, final y_value will be used to interpolate x and y
      and run variational method with final and interpolated y on
      new x-values as initial values. Processes will be repeated n_interpolations
      times. Default is 0.

  Returns
  -------
  ndarray
      Approximation of y(x) at the given values of x.
  """

  def lattice_sweep(x, S, init, omega, h):
    """
    Sweep over all x and calculate y.

    Parameters
    ----------
    x : ndarray
        x-values over which to integrate the ODE. Must have len(x)%4 == 0
    S : function
        Source term S(x) in (*).
    init: ndarray
        Initial values at all x.
    omega : float
        Convergence condition. Must be between 0 and 2.
    h : float
        Step size, i.e. distance between x-values.

    Returns
    -------
    ndarray
        Approximation of y(x) after lattice sweep n at the given values of x.
    """

    yn = init.copy()
    Sn = S(x)
    for i in range(1, len(yn) - 1):
      y_old = yn[i]
      y_improved = 1/2*(yn[i - 1] + yn[i + 1] + h**2*Sn[i])
      y_new = (1 - omega)*y_old + omega*y_improved
      yn[i] = y_new

    return yn

  def calculate_energy(x, y, S, h):
    """
    Calculate energy for y from all lattice sweeps.

    Parameters
    ----------
    x : ndarray
        x-values over which to integrate the ODE. Must have len(x)%4 == 0
    y : ndarray
        Calculated y(x) at given values of x for all lattice sweeps.
    S : function
        Source term S(x) in (*).
    h : float
        Step size, i.e. distance between x-values.

    Returns
    -------
    ndarray
        Energy of system for each lattice sweep.
    """

    y0 = y[:, :-1]
    y1 = y[:, 1: ]
    Sn = S(x)
    return 1/(2*h) * np.sum((y1 - y0)**2, axis=1) - h*np.sum(y1 * Sn[1:], axis=1)

  def linear_interpolation(x, y_final):
    """
    Generate new initial by interpolation of final y(x) from previous iterations.

    Parameters
    ----------
    x : ndarray
        x-values over which to integrate the ODE. Must have len(x)%4 == 0
    y_final : y(x) from last lattice sweep of previous round of iterations.
    h : float
        Step size, i.e. distance between x-values.

    Returns
    -------
    ndarray
        New set of lattice points and initial values after interpolation.
    """

    x0 = x[:-1]
    x1 = x[1:]
    y0 = y_final[:-1]
    y1 = y_final[1:]

    x_mid = x0 + (x1 - x0)/2
    y_mid = y0 + (x_mid - x0)*(y1 - y0)/(x1 - x0)

    init_new = np.zeros(2*len(y_final) - 1)
    init_new[::2] = y_final
    init_new[1::2] = y_mid

    x_new = np.zeros(2*len(x) - 1)
    x_new[::2] = x
    x_new[1::2] = x_mid
    
    return x_new, init_new

  y = np.vstack((init,))
  for i in range(n_sweeps):
    y = np.vstack((y, lattice_sweep(x, S, y[-1], omega, h)))

  if n_interpolations > 0:
      x, init = linear_interpolation(x, y[-1])
      n_interpolations -= 1
      return variational_method(x, S, init, omega, h, n_sweeps, n_interpolations)

  import matplotlib.pyplot as plt
  plt.plot(x, y[-1])
  plt.show()
  E = calculate_energy(x, y, S, h)
  return y, E
