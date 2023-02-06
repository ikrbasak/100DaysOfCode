# https://projecteuler.net/problem=85
# https://github.com/ikrbasak/100DaysOfCode
# 06-02-2023

import math


def num_rectangles(m, n):
    return (m + 1) * m * (n + 1) * n // 4


def solution():
    TARGET = 2000000
    end = int(math.sqrt(TARGET)) + 1
    gen = ((w, h) for w in range(1, end) for h in range(1, end))
    func = lambda wh: abs(num_rectangles(*wh) - TARGET)
    ans = min(gen, key=func)
    return ans[0] * ans[1]


if __name__ == "__main__":
    print(solution())
