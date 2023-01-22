# https://projecteuler.net/problem=10
# https://github.com/ikrbasak/100DaysOfCode
# 22-01-2023

from math import sqrt


def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


def list_primes(num: int) -> list:
    return [x for x in range(num + 1) if is_prime(x)]


def solution():
    ans = sum(list_primes(1999999))
    return ans


if __name__ == "__main__":
    print(solution())
