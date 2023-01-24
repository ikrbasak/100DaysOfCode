# https://projecteuler.net/problem=16
# https://github.com/ikrbasak/100DaysOfCode
# 24-01-2023


def solution():
    n = 2**1000
    ans = sum(int(c) for c in str(n))
    return ans


if __name__ == "__main__":
    print(solution())
