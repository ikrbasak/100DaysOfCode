# https://projecteuler.net/problem=2
# https://github.com/ikrbasak/100DaysOfCode
# 21-01-2023


def solution():
    ans = 0
    x = 1
    y = 2
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    return ans


if __name__ == "__main__":
    print(solution())
