# https://projecteuler.net/problem=4
# https://github.com/ikrbasak/100DaysOfCode
# 21-01-2023


def solution():
    ans = max(
        i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i * j) == str(i * j)[::-1]
    )
    return ans


if __name__ == "__main__":
    print(solution())
