# https://projecteuler.net/problem=58
# https://github.com/ikrbasak/100DaysOfCode
# 01-02-2023

import fractions
import itertools
from math import sqrt


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


def solution():
    TARGET = fractions.Fraction(1, 10)
    numprimes = 0
    for n in itertools.count(1, 2):
        for i in range(4):
            if is_prime(n * n - i * (n - 1)):
                numprimes += 1
        if n > 1 and fractions.Fraction(numprimes, n * 2 - 1) < TARGET:
            return n


if __name__ == "__main__":
    print(solution())
