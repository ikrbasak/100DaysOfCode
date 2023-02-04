# https://projecteuler.net/problem=71
# https://github.com/ikrbasak/100DaysOfCode
# 04-02-2023


def solution():
    LIMIT = 1000000
    maxnumer = 0
    maxdenom = 1
    for d in range(1, LIMIT + 1):
        n = d * 3 // 7
        if d % 7 == 0:
            n -= 1
        if n * maxdenom > d * maxnumer:
            maxnumer = n
            maxdenom = d
    return maxnumer


if __name__ == "__main__":
    print(solution())
