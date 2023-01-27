# https://projecteuler.net/problem=32
# https://github.com/ikrbasak/100DaysOfCode
# 27-01-2023

import math


def has_pandigital_product(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


def solution():
    ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
    return ans


if __name__ == "__main__":
    print(solution())
