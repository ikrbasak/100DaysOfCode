# https://projecteuler.net/problem=52
# https://github.com/ikrbasak/100DaysOfCode
# 31-01-2023

import itertools


def solution():
    cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))
    ans = next(i for i in itertools.count(1) if cond(i))
    return ans


if __name__ == "__main__":
    print(solution())
