# https://projecteuler.net/problem=34
# https://github.com/ikrbasak/100DaysOfCode
# 27-01-2023

import math


def factorial_digit_sum(n):
    result = 0
    while n >= 10000:
        result += FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS[n % 10000]
        n //= 10000
    return result + FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS[n]


def solution():
    ans = sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i))
    return ans


FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS = [
    sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)
]
FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS = [
    sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)
]

if __name__ == "__main__":
    print(solution())
