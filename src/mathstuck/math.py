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
    if x < 0:
        ValueError("sqrtLessThanZero")
        return

    if x == 0:
        return 0

    k = x
    for i in range(100):
        k = ((x - 1) * (k / x)) + (x / (x * (k ** (x - 1))))

    return k


def cos(x):
    """The function returns cosinus of x
       """
    xold = x
    x = 0
    minus = 1
    for i in range(0, 2,200):
        x += minus * ((xold ** i) / fact(i))
        minus *= -1

    return x


def sin(x):
    """The function returns sinus of x
       """
    xold = x
    minus = -1
    for i in range(3, 200, 2):
        x += minus * ((xold ** i) / fact(i))
        minus *= -1

    return x
