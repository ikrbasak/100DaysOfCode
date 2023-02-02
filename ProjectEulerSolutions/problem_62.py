# https://projecteuler.net/problem=62
# https://github.com/ikrbasak/100DaysOfCode
# 02-02-2023

import itertools


def solution():
    numdigits = 0
    data = {}
    for i in itertools.count():
        digits = [int(c) for c in str(i**3)]
        digits.sort()
        numclass = "".join(str(d) for d in digits)

        if len(numclass) > numdigits:
            candidates = [lowest for (lowest, count) in data.values() if count == 5]
            if len(candidates) > 0:
                return str(min(candidates) ** 3)
            data = {}
            numdigits = len(numclass)

        lowest, count = data.get(numclass, (i, 0))
        data[numclass] = (lowest, count + 1)


if __name__ == "__main__":
    print(solution())
