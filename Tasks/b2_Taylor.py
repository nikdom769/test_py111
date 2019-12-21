"""
Taylor series
"""
import itertools
import math
from typing import Union



def ex(x: Union[int, float], delta=0.0001) -> float:
    """
    Calculate value of e^x with Taylor series
    :param x: x value
    :return: e^x value
    """
    result = 1.0
    # delta - точность вычисления
    if x == 0:
        return 1
    else:
        for n in itertools.count(1, 1):
            result += (x**n / math.factorial(n))
            if delta > (x**n / math.factorial(n)):
                break
        print(x)
        return result


def sinx(x: Union[int, float], delta=0.0001) -> float:
    """
    Calculate sin(x) with Taylor series
    :param x: x value
    :return: sin(x) value
    """
    result = x
    if x == 0:
        return 0
    else:
        for i in itertools.count(1, 1):
            n = 2 * i + 1
            result += ((-1)**i)*(x**n / math.factorial(n))
            if delta > (x**i / math.factorial(i)):
                break
        print(x)
        return result

