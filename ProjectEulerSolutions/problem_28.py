# https://projecteuler.net/problem=28
# https://github.com/ikrbasak/100DaysOfCode
# 26-01-2023


def solution():
    SIZE = 1001
    ans = 1
    ans += sum(4 * i * i - 6 * (i - 1) for i in range(3, SIZE + 1, 2))
    return ans


if __name__ == "__main__":
    print(solution())
