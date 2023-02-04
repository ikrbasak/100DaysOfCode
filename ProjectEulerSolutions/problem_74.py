# https://projecteuler.net/problem=74
# https://github.com/ikrbasak/100DaysOfCode
# 04-02-2023

import math


def factorialize(n):
    result = 0
    while n != 0:
        result += FACTORIAL[n % 10]
        n //= 10
    return result


def get_chain_length(n):
    seen = set()
    while True:
        seen.add(n)
        n = factorialize(n)
        if n in seen:
            return len(seen)


def solution():
    LIMIT = 10**6
    ans = sum(1 for i in range(LIMIT) if get_chain_length(i) == 60)
    return ans


FACTORIAL = [math.factorial(i) for i in range(10)]

if __name__ == "__main__":
    print(solution())
