# https://projecteuler.net/problem=12
# https://github.com/ikrbasak/100DaysOfCode
# 23-01-2023


import itertools
import math


def num_divisors(n):
    end = int(math.sqrt(n))
    result = sum(2 for i in range(1, end + 1) if n % i == 0)
    if end**2 == n:
        result -= 1
    return result


def solution():
    triangle = 0
    for i in itertools.count(1):
        triangle += i
        if num_divisors(triangle) > 500:
            return triangle


if __name__ == "__main__":
    print(solution())
