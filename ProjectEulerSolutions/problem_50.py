# https://projecteuler.net/problem=50
# https://github.com/ikrbasak/100DaysOfCode
# 30-01-2023

from math import sqrt


def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(sqrt(n)) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def solution():
    ans = 0
    isprime = list_primality(999999)
    primes = [i for (i, isprime) in enumerate(isprime) if isprime]
    consecutive = 0
    for i in range(len(primes)):
        sum = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            consec += 1
            if sum >= len(isprime):
                break
            if isprime[sum] and consec > consecutive:
                ans = sum
                consecutive = consec
    return ans


if __name__ == "__main__":
    print(solution())
