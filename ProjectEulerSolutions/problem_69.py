# https://projecteuler.net/problem=69
# https://github.com/ikrbasak/100DaysOfCode
# 03-02-2023


import fractions


def list_totients(n: int):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result


def solution():
    totients = list_totients(10**6)
    ans = max(
        range(2, len(totients)), key=(lambda i: fractions.Fraction(i, totients[i]))
    )
    return ans


if __name__ == "__main__":
    print(solution())
