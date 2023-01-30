# https://projecteuler.net/problem=47
# https://github.com/ikrbasak/100DaysOfCode
# 30-01-2023


import functools
import itertools
from math import sqrt


@functools.cache
def count_distinct_prime_factors(n):
    count = 0
    while n > 1:
        count += 1
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
                break
        else:
            break
    return count


def solution():
    cond = lambda i: all((count_distinct_prime_factors(i + j) == 4) for j in range(4))
    ans = next(filter(cond, itertools.count()))
    return ans


if __name__ == "__main__":
    print(solution())
