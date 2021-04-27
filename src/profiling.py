

# ########################################
# Brief: File used for profiling
# Project: Calculator
# File: profiling.py
# File Author/s: Roman Országh <xorsza01(at)fit.vutbr.cz>
# Project Authors: Stanislav Gabriš <xgabri18(at)fit.vutbr.cz>
#                  Roman Országh <xorsza01(at)fit.vutbr.cz>
#                  Jarolím Antonín <xjarol06(at)fit.vutbr.cz>
# 			       Vlk Jakub <xvlkja07(at)fit.vutbr.cz>
# ########################################


import sys
import lib.mathstuck.mathcore as math


def standard_deviation(numbers):
    """! Calculate the standard deviation from numbers.

    @param numbers: Numbers that are passed from input
    @return Result of standard deviation.
    """
    x = numbers
    N = len(numbers)

    mean = arithmetic_mean(numbers, N)
    mean = math.exp(mean, 2)

    sum_x = 0
    for i in range(N):
        x[i] = math.exp(x[i], 2)
        sum_x = math.add(sum_x, x[i])

    result = math.sub(sum_x, math.mul(N, mean))
    result = math.div(result, math.sub(N, 1))
    result = math.sqrt(result, 2)
    return result


def arithmetic_mean(x, N):
    """! Calculate the arithmetic mean

    @param x: List of 'x' numbers
    @param N: Number of 'x' numbers
    @return
    """
    sum_x = 0
    for i in range(N):
        sum_x = math.add(sum_x, x[i])
    result = math.div(sum_x, N)
    return result


def main():
    data = list()

    for line in sys.stdin:
        line = line.strip().split(' ')
        for item in line:
            if item != '':
                data.append(int(item))

    print(standard_deviation(data))


if __name__ == '__main__':
    main()
