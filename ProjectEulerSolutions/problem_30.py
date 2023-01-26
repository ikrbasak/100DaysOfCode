# https://projecteuler.net/problem=30
# https://github.com/ikrbasak/100DaysOfCode
# 26-01-2023


def fifth_power_digit_sum(n):
    return sum(int(c) ** 5 for c in str(n))


def solution():
    ans = sum(i for i in range(2, 1000000) if i == fifth_power_digit_sum(i))
    return ans


if __name__ == "__main__":
    print(solution())
