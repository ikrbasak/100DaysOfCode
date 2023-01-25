# https://projecteuler.net/problem=24
# https://github.com/ikrbasak/100DaysOfCode
# 25-01-2023

import itertools


def solution():
    arr = list(range(10))
    temp = itertools.islice(itertools.permutations(arr), 999999, None)
    return "".join(str(x) for x in next(temp))


if __name__ == "__main__":
    print(solution())
