# https://projecteuler.net/problem=19
# https://github.com/ikrbasak/100DaysOfCode
# 24-01-2023

import datetime


def solution():
    ans = sum(
        1
        for y in range(1901, 2001)
        for m in range(1, 13)
        if datetime.date(y, m, 1).weekday() == 6
    )
    return ans


if __name__ == "__main__":
    print(solution())
