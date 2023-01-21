# https://projecteuler.net/problem=1
# https://github.com/ikrbasak/100DaysOfCode
# 21-01-2023


def solution():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return ans


if __name__ == "__main__":
    print(solution())
