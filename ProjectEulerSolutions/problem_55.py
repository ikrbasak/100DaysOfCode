# https://projecteuler.net/problem=55
# https://github.com/ikrbasak/100DaysOfCode
# 31-01-2023


def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


def solution():
    ans = sum(1 for i in range(10000) if is_lychrel(i))
    return ans


if __name__ == "__main__":
    print(solution())
