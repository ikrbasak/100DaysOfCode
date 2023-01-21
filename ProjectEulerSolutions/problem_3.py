# https://projecteuler.net/problem=3
# https://github.com/ikrbasak/100DaysOfCode
# 21-01-2023

import math


def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


def solution():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n //= p
        else:
            return n


if __name__ == "__main__":
    print(solution())
