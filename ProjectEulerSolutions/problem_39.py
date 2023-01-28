# https://projecteuler.net/problem=39
# https://github.com/ikrbasak/100DaysOfCode
# 28-01-2023


def count_solutions(p):
    result = 0
    for a in range(1, p + 1):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b
            if a * a + b * b == c * c:
                result += 1
    return result


def solution():
    ans = max(range(1, 1001), key=count_solutions)
    return ans


if __name__ == "__main__":
    print(solution())
