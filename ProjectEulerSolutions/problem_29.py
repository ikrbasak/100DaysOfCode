# https://projecteuler.net/problem=29
# https://github.com/ikrbasak/100DaysOfCode
# 26-01-2023


def solution():
    seen = set(a ** b for a in range(2, 101) for b in range(2, 101))
    return len(seen)


if __name__ == "__main__":
    print(solution())
