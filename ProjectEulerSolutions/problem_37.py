# https://projecteuler.net/problem=37
# https://github.com/ikrbasak/100DaysOfCode
# 28-01-2023

import itertools
from math import sqrt


def is_prime(x):
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


def is_truncatable_prime(n):
    i = 10
    while i <= n:
        if not is_prime(n % i):
            return False
        i *= 10

    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True


def solution():
    ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
    return ans


if __name__ == "__main__":
    print(solution())
