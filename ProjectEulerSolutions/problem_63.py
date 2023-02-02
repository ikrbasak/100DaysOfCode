# https://projecteuler.net/problem=63
# https://github.com/ikrbasak/100DaysOfCode
# 02-02-2023


def solution():
    ans = sum(1 for i in range(1, 10) for j in range(1, 22) if len(str(i**j)) == j)
    return ans


if __name__ == "__main__":
    print(solution())
