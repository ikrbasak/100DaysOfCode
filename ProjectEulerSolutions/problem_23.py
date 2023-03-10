# https://projecteuler.net/problem=23
# https://github.com/ikrbasak/100DaysOfCode
# 25-01-2023


def solution():
    LIMIT = 28124
    divisorsum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]

    expressible = [False] * LIMIT
    for i in abundantnums:
        for j in abundantnums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break

    ans = sum(i for (i, x) in enumerate(expressible) if not x)
    return ans


if __name__ == "__main__":
    print(solution())
