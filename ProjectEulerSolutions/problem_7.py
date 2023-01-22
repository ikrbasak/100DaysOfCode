# https://projecteuler.net/problem=7
# https://github.com/ikrbasak/100DaysOfCode
# 22-01-2023


import itertools
from math import sqrt


def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


def solution():
    ans = next(itertools.islice(filter(is_prime, itertools.count(2)), 10000, None))
    return ans


if __name__ == "__main__":
    print(solution())
