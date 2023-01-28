# https://projecteuler.net/problem=36
# https://github.com/ikrbasak/100DaysOfCode
# 28-01-2023


def is_decimal_binary_palindrome(n):
    s = str(n)
    if s != s[::-1]:
        return False
    t = bin(n)[2:]
    return t == t[::-1]


def solution():
    ans = sum(i for i in range(1000000) if is_decimal_binary_palindrome(i))
    return ans


if __name__ == "__main__":
    print(solution())
