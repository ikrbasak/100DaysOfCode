# https://projecteuler.net/problem=80
# https://github.com/ikrbasak/100DaysOfCode
# 05-02-2023


def dSum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


def fastRoot(n):
    a = 5 * n
    b = 5
    limit = 10**101
    while b < limit:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b - b % 10) * 10 + b % 10

    root = int(str(b)[:100])
    return root


def solution():
    result = 0
    for n in range(1, 101):
        if n not in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
            rootN = fastRoot(n)
            result += dSum(rootN)
    return result


if __name__ == "__main__":
    print(solution())
