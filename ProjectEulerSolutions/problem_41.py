# https://projecteuler.net/problem=41
# https://github.com/ikrbasak/100DaysOfCode
# 29-01-2023

import math


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


def prev_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(arr) - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
    return True


def solution():
    for n in reversed(range(2, 10)):
        arr = list(reversed(range(1, n + 1)))
        while True:
            if arr[-1] not in NONPRIME_LAST_DIGITS:
                n = int("".join(str(x) for x in arr))
                if is_prime(n):
                    return n
            if not prev_permutation(arr):
                break
    raise AssertionError()


NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}

if __name__ == "__main__":
    print(solution())
