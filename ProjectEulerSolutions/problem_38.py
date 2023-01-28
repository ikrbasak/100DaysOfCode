# https://projecteuler.net/problem=38
# https://github.com/ikrbasak/100DaysOfCode
# 28-01-2023


def solution():
    ans = ""
    for n in range(2, 10):
        for i in range(1, 10 ** (9 // n)):
            s = "".join(str(i * j) for j in range(1, n + 1))
            if "".join(sorted(s)) == "123456789":
                ans = max(s, ans)
    return ans


if __name__ == "__main__":
    print(solution())
