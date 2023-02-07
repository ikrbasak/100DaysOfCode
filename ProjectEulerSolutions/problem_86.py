# https://projecteuler.net/problem=86
# https://github.com/ikrbasak/100DaysOfCode
# 07-02-2023

import itertools
import math


def solution():
    solutions = []

    def generate_solutions():
        for s in itertools.count(3, 2):
            for t in range(s - 2, 0, -2):
                if s * s // 2 >= limit * 3:
                    return

                if math.gcd(s, t) == 1:
                    for k in itertools.count(1):
                        a = s * t * k
                        b = (s * s - t * t) // 2 * k
                        c = (s * s + t * t) // 2 * k
                        if a >= limit and b >= limit:
                            break
                        find_splits(a, b, c)
                        find_splits(b, a, c)

    def find_splits(a, b, c):
        z = b
        for x in range(1, a):
            y = a - x
            if y < x:
                break
            if c * c == min(
                (x + y) * (x + y) + z * z,
                (y + z) * (y + z) + x * x,
                (z + x) * (z + x) + y * y,
            ):
                temp = max(x, y, z)
                if temp < limit:
                    item = tuple(sorted((x, y, z)))
                    solutions[temp].add(item)

    cumulativesolutions = [0]

    limit = 1
    while True:
        while len(solutions) < limit:
            solutions.append(set())

        generate_solutions()

        for i in range(len(cumulativesolutions), limit):
            sum = cumulativesolutions[i - 1] + len(solutions[i])
            cumulativesolutions.append(sum)
            if sum > 1000000:
                return i

        limit *= 2


if __name__ == "__main__":
    print(solution())
