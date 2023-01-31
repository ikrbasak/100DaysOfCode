# https://projecteuler.net/problem=53
# https://github.com/ikrbasak/100DaysOfCode
# 31-01-2023

import math


def binomial(n: int, k: int) -> int:
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def solution():
    ans = sum(
        1 for n in range(1, 101) for k in range(0, n + 1) if binomial(n, k) > 1000000
    )
    return ans


if __name__ == "__main__":
    print(solution())
