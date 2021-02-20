"""
A collection of simple math operations.
"""

def simple_add(a,b):
    """
    Sum two numers.

    Parameters
    ----------
    a : float
    b : float

    Returns
    -------
    float
        Sum of a and b.

    Examples
    --------
    >>> simple_add(1, 1)
    2
    """

    return a+b

def simple_sub(a,b):
    """
    Subtract two numers.

    Parameters
    ----------
    a : float
    b : float

    Returns
    -------
    float
        Difference between a and b.

    Examples
    --------
    >>> simple_sub(1, 1)
    0
    """

    return a-b

def simple_mult(a,b):
    """
    Product of two numers.

    Parameters
    ----------
    a : float
    b : float

    Returns
    -------
    float
        Product of a and b.

    Examples
    --------
    >>> simple_mult(2, 3)
    6
    """

    return a*b

def simple_div(a,b):
    """
    Quotient of two numers.

    Parameters
    ----------
    a : float
    b : float

    Returns
    -------
    float
        Quotient of a and b.

    Examples
    --------
    >>> simple_div(6, 2)
    3
    """

    return a/b

def poly_first(x, a0, a1):
    """
    First order polynomial.

    Parameters
    ----------
    x :  array_like
         x-coordinates at which polynomial is to be defined.
    a0 : float
         Zeroth order coeffient.
    a1 : float
         First order coefficient.

    Returns
    -------
    array_like
        Polynomial on the form a0 + a1*x.

    Examples
    --------
    >>> import numpy as np
    >>> x = np.array([1, 2, 3])
    >>> poly_first(x, 1, 2)
    array([3, 5, 7])
    """

    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    First order polynomial.

    Parameters
    ----------
    x :  array_like
         x-coordinates at which polynomial is to be defined.
    a0 : float
         Zeroth order coeffient.
    a1 : float
         First order coefficient.
    a2 : float
         Second order coefficient.

    Returns
    -------
    array_like
        Polynomial on the form a0 + a1*x + a2*(x**2).

    Examples
    --------
    >>> import numpy as np
    >>> x = np.array([1, 2, 3])
    >>> poly_first(x, 1, 2, 3)
    array([6, 17, 34])
    """
    return poly_first(x, a0, a1) + a2*(x**2)
