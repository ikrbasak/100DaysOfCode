# https://projecteuler.net/problem=77
# https://github.com/ikrbasak/100DaysOfCode
# 05-02-2023

import itertools
from math import sqrt

primes = [2]


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


def num_prime_sum_ways(n):
    for i in range(primes[-1] + 1, n + 1):
        if is_prime(i):
            primes.append(i)

    ways = [1] + [0] * n
    for p in primes:
        for i in range(n + 1 - p):
            ways[i + p] += ways[i]
    return ways[n]


def solution():
    cond = lambda n: num_prime_sum_ways(n) > 5000
    ans = next(filter(cond, itertools.count(2)))
    return ans


if __name__ == "__main__":
    print(solution())
