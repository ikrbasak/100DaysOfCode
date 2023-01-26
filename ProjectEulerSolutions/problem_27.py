# https://projecteuler.net/problem=27
# https://github.com/ikrbasak/100DaysOfCode
# 26-01-2023

import itertools
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3, int(sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True


def count_consecutive_primes(ab):
    a, b = ab
    for i in itertools.count():
        n = i * i + i * a + b
        if not is_prime(n):
            return i


def solution():
    ans = max(
        ((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
        key=count_consecutive_primes,
    )
    return ans[0] * ans[1]


if __name__ == "__main__":
    print(solution())
