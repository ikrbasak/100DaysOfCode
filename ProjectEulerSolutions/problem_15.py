# https://projecteuler.net/problem=15
# https://github.com/ikrbasak/100DaysOfCode
# 23-01-2023

import math


def binomial(n: int, k: int) -> int:
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def solution():
    return binomial(40, 20)


if __name__ == "__main__":
    print(solution())
