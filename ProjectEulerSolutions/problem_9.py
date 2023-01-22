# https://projecteuler.net/problem=9
# https://github.com/ikrbasak/100DaysOfCode
# 22-01-2023


def solution():
    PERIMETER = 1000
    for a in range(1, PERIMETER + 1):
        for b in range(a + 1, PERIMETER + 1):
            c = PERIMETER - a - b
            if a * a + b * b == c * c:
                return a * b * c


if __name__ == "__main__":
    print(solution())
