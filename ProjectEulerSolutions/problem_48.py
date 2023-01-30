# https://projecteuler.net/problem=48
# https://github.com/ikrbasak/100DaysOfCode
# 30-01-2023


def solution():
    MOD = 10**10
    ans = sum(pow(i, i, MOD) for i in range(1, 1001)) % MOD
    return ans


if __name__ == "__main__":
    print(solution())
