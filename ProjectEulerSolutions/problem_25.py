# https://projecteuler.net/problem=25
# https://github.com/ikrbasak/100DaysOfCode
# 25-01-2023

import itertools


def solution():
    DIGITS = 1000
    prev = 1
    cur = 0
    for i in itertools.count():
        if len(str(cur)) > DIGITS:
            raise RuntimeError("Not found")
        elif len(str(cur)) == DIGITS:
            return i

        prev, cur = cur, prev + cur


if __name__ == "__main__":
    print(solution())
