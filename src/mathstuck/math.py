"""@package docstring
Custom math library for IVS project.
"""


def add(a, b):
    """The function returns the value a plus b.
       """
    return a + b


def sub(a, b):
    """The function returns the value a minus b
       """
    return a - b


def div(a, b):
    """The function returns the value a divided by b
       """
    if b == 0:
        ValueError("DividedByZero")
        return
    return a / b


def mul(a, b):
    """The function returns the value of a multiplied by b
       """
    return a * b


def exp(a, b):
    """TheThe function returns the value a raised to the power of b
       """
    return a ** b


def sqrt(x, n):
    """the function returns the nth root of the x value
       """
    if x < 0:
        ValueError("sqrtLessThanZero")
        return

    if x == 0:
        return 0

    k = n
    for i in range(100):
        k = ((n - 1) * (k / n)) + (x / (n * (k ** (n - 1))))

    return k


def fact(x):
    """The function returns factorial of x
       """
    res = 1
    for i in range(1, x + 1):
        res *= i

    return res


def cos(x):
    """The function returns cosinus of x
       """
    xrad = x / 180 * pi()
    x= 1
    minus = -1
    for i in range(2, 150, 2):
        factr = fact(i)
        heh = (xrad ** i) / factr
        x += minus * heh
        minus *= -1

    return x


def sin(x):
    """The function returns sinus of x
       """
    xrad = x / 180 * pi()
    x= xrad
    minus = -1
    for i in range(3, 150, 2):
        factr = fact(i)
        heh = (xrad ** i) / factr
        x += minus * heh
        minus *= -1

    return x


def pi():
    pi = 3
    minus = 1
    for i in range (2, 1000, 2):
        div = i* (i+1) * (i+2)
        pi += minus * 4 / div
        minus *= -1

    return pi
