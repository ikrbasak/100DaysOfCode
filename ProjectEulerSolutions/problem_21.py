# https://projecteuler.net/problem=21
# https://github.com/ikrbasak/100DaysOfCode
# 25-01-2023


def solution():
    divisorsum = [0] * 10000
    for i in range(1, len(divisorsum)):
        for j in range(i * 2, len(divisorsum), i):
            divisorsum[j] += i

    ans = 0
    for i in range(1, len(divisorsum)):
        j = divisorsum[i]
        if j != i and j < len(divisorsum) and divisorsum[j] == i:
            ans += i
    return ans


if __name__ == "__main__":
    print(solution())
