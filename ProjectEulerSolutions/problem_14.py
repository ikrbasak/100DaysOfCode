# https://projecteuler.net/problem=14
# https://github.com/ikrbasak/100DaysOfCode
# 23-01-2023


import functools
import sys


@functools.cache
def collatz_chain_length(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    return collatz_chain_length(y) + 1


def solution():
    sys.setrecursionlimit(3000)
    ans = max(range(1, 1000000), key=collatz_chain_length)
    return ans


if __name__ == "__main__":
    print(solution())
