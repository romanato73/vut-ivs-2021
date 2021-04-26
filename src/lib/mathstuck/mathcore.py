"""! Custom math library for IVS project.
"""

# ########################################
# Brief: Core library with mathematical operations
# Project: Calculator
# File: mathcore.py
# File Author/s: Vlk Jakub <xvlkja07(at)fit.vutbr.cz> , Jarolím Antonín <xjarol06(at)fit.vutbr.cz>
# Project Authors: Stanislav Gabriš <xgabri18(at)fit.vutbr.cz>
#                  Roman Országh <xorsza01(at)fit.vutbr.cz>
#                  Jarolím Antonín <xjarol06(at)fit.vutbr.cz>
# 			       Vlk Jakub <xvlkja07(at)fit.vutbr.cz>
# ########################################


def add(a, b):
    """! The function returns the value a plus b.

    @param a: First number
    @param b: Second number
    @return Sum of two numbers.
    """
    return a + b


def sub(a, b):
    """! The function returns the value a minus b

    @param a: First number
    @param b: Second number
    @return Difference of two numbers.
    """
    return a - b


def div(a, b):
    """! The function returns the value a divided by b

    @param a: First number
    @param b: Second number
    @return Division of two numbers.
    """
    if b == 0:
        raise ValueError("DividedByZero")
    return a / b


def mul(a, b):
    """! The function returns the value of a multiplied by b

    @param a: First number
    @param b: Second number
    @return Multiplication of two numbers.
    """
    return a * b


def exp(x, n):
    """! The function returns the value a raised to the power of b

    @param x: First number
    @param n: Second number
    @return n-th power of number x.
    """
    return x ** n


def sqrt(x, n):
    """! The function returns the nth root of the x value

    @param x: First number
    @param n: Second number
    @return n-th root of number x.
    """
    if x < 0:
        raise ValueError("sqrtLessThanZero")

    if x == 0:
        return 0

    if x == 1:
        return 1

    k = n
    for i in range(100):
        k = ((n - 1) * (k / n)) + (x / (n * (k ** (n - 1))))

    return k


def fact(x):
    """! The function returns factorial of x

    @param x: Factored number
    @return Factorial of number x
    """
    minus = 1
    if x < 0:
        minus = -1
        x *= minus

    if x == 0:
        return 1

    res = 1
    for i in range(1, x + 1):
        res *= i

    return res * minus


def cos(x):
    """! The function returns cosine of x

    @param x: Variable x
    @return Cosine of number x.
    """
    xrad = x / 180 * pi()
    x = 1
    minus = -1
    for i in range(2, 150, 2):
        factr = fact(i)
        heh = (xrad ** i) / factr
        x += minus * heh
        minus *= -1

    x = round(x, 8)
    if 1e-8 > x > -1e-8:
        return 0

    return x


def sin(x):
    """! The function returns sine o x

    @param x: Variable x
    @return Sine of number x.
    """
    xrad = x / 180 * pi()
    x = xrad
    minus = -1
    for i in range(3, 150, 2):
        factr = fact(i)
        heh = (xrad ** i) / factr
        x += minus * heh
        minus *= -1

    if 1e-8 > x > -1e-8:
        return 0

    return x


def pi():
    """! This function returns the representation of pi constant

    @return: Float value of pi constant
    """
    value = 3
    minus = 1
    for i in range(2, 1000, 2):
        divisor = i * (i + 1) * (i + 2)
        value += minus * 4 / divisor
        minus *= -1

    return value
