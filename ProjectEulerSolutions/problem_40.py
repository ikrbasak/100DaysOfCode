# https://projecteuler.net/problem=40
# https://github.com/ikrbasak/100DaysOfCode
# 28-01-2023


def solution():
    s = "".join(str(i) for i in range(1, 1000000))
    ans = 1
    for i in range(7):
        ans *= int(s[10 ** i - 1])
    return ans


if __name__ == "__main__":
    print(solution())
