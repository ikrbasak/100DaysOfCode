# https://projecteuler.net/problem=88
# https://github.com/ikrbasak/100DaysOfCode
# 07-02-2023


def solution():
    LIMIT = 12000
    minsumproduct = [None] * (LIMIT + 1)

    def factorize(n, remain, maxfactor, sum, terms):
        if remain == 1:
            if sum > n:
                raise AssertionError()
            terms += n - sum
            if terms <= LIMIT and (
                minsumproduct[terms] is None or n < minsumproduct[terms]
            ):
                minsumproduct[terms] = n
        else:
            for i in range(2, maxfactor + 1):
                if remain % i == 0:
                    factor = i
                    factorize(
                        n,
                        remain // factor,
                        min(factor, maxfactor),
                        sum + factor,
                        terms + 1,
                    )

    for i in range(2, LIMIT * 2 + 1):
        factorize(i, i, i, 0, 0)

    ans = sum(set(minsumproduct[2:]))
    return ans


if __name__ == "__main__":
    print(solution())
