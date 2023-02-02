# https://projecteuler.net/problem=65
# https://github.com/ikrbasak/100DaysOfCode
# 02-02-2023


def e_contfrac_term(i):
    if i == 0:
        return 2
    elif i % 3 == 2:
        return i // 3 * 2 + 2
    else:
        return 1


def solution():
    numer = 1
    denom = 0
    for i in reversed(range(100)):
        numer, denom = e_contfrac_term(i) * numer + denom, numer
    ans = sum(int(c) for c in str(numer))
    return ans


if __name__ == "__main__":
    print(solution())
