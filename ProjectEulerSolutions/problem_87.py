# https://projecteuler.net/problem=87
# https://github.com/ikrbasak/100DaysOfCode
# 07-02-2023

import math


def list_primality(n: int):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def list_primes(n: int):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


def solution():
    LIMIT = 50000000
    primes = list_primes(int(math.sqrt(LIMIT)))

    sums = {0}
    for i in range(2, 5):
        newsums = set()
        for p in primes:
            q = p**i
            if q > LIMIT:
                break
            for x in sums:
                if x + q <= LIMIT:
                    newsums.add(x + q)
        sums = newsums
    return len(sums)


if __name__ == "__main__":
    print(solution())
