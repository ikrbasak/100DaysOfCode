# https://projecteuler.net/problem=35
# https://github.com/ikrbasak/100DaysOfCode
# 27-01-2023


def primes_upto(n):
    if n < 2:
        return
    marked = [0] * (n + 1)
    value = 3
    yield 2
    while value <= n:
        if marked[value] == 0:
            yield value
            i = value
            while i <= n:
                marked[i] = 1
                i += value
        value += 2


def primes_under(n):
    return primes_upto(n - 1)


def num_digits(n):
    if n < 0:
        return num_digits(-n)
    if n < 10:
        return 1
    return 1 + num_digits(n // 10)


def rotate(n):
    right = n % 10
    left = n // 10
    for _ in range(num_digits(n) - 1):
        right *= 10
    return right + left


def rotations(n):
    yield n
    x = rotate(n)
    while x != n:
        yield x
        x = rotate(x)


def is_circular_prime(n, P):
    for i in rotations(n):
        if i not in P:
            return False
    return True


def circular_primes(P):
    for i in P:
        if is_circular_prime(i, P):
            yield i


def solution():
    P = set(primes_under(1000000))
    C = set(circular_primes(P))
    return len(C)


if __name__ == "__main__":
    print(solution())
