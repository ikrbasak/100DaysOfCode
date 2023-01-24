# https://projecteuler.net/problem=20
# https://github.com/ikrbasak/100DaysOfCode
# 24-01-2023

import math


def solution():
    n = math.factorial(100)
    ans = sum(int(c) for c in str(n))
    return ans


if __name__ == "__main__":
    print(solution())
