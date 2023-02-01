# https://projecteuler.net/problem=56
# https://github.com/ikrbasak/100DaysOfCode
# 01-02-2023


def solution():
    ans = max(sum(int(c) for c in str(a**b)) for a in range(100) for b in range(100))
    return ans


if __name__ == "__main__":
    print(solution())
