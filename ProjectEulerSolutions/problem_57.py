# https://projecteuler.net/problem=57
# https://github.com/ikrbasak/100DaysOfCode
# 01-02-2023


def solution():
    LIMIT = 1000
    ans = 0
    numer = 0
    denom = 1
    for _ in range(LIMIT):
        numer, denom = denom, denom * 2 + numer
        if len(str(numer + denom)) > len(str(denom)):
            ans += 1
    return ans


if __name__ == "__main__":
    print(solution())
