# https://projecteuler.net/problem=5
# https://github.com/ikrbasak/100DaysOfCode
# 21-01-2023


import math


def solution():
    ans = 1
    for i in range(1, 21):
        ans *= i // math.gcd(i, ans)
    return ans


if __name__ == "__main__":
    print(solution())
