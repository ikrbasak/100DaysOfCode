# https://projecteuler.net/problem=75
# https://github.com/ikrbasak/100DaysOfCode
# 04-02-2023

import math


def solution():
    LIMIT = 1500000
    triples = set()
    for s in range(3, int(math.sqrt(LIMIT)) + 1, 2):
        for t in range(s - 2, 0, -2):
            if math.gcd(s, t) == 1:
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2
                if a + b + c <= LIMIT:
                    triples.add((a, b, c))

    ways = [0] * (LIMIT + 1)
    for triple in triples:
        sigma = sum(triple)
        for i in range(sigma, len(ways), sigma):
            ways[i] += 1

    ans = ways.count(1)
    return ans


if __name__ == "__main__":
    print(solution())
