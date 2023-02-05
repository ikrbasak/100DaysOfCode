# https://projecteuler.net/problem=79
# https://github.com/ikrbasak/100DaysOfCode
# 05-02-2023

import itertools


def is_consistent(guess):
    return all(is_subsequence(s, guess) for s in SUBSEQS)


def is_subsequence(shortstr, longstr):
    i = 0
    for c in longstr:
        if c == shortstr[i]:
            i += 1
            if i == len(shortstr):
                return True
    return False


def solution():
    charsused = sorted(set().union(*SUBSEQS))
    base = len(charsused)

    for length in itertools.count(base):
        indices = [0] * length
        while True:
            guess = "".join(charsused[d] for d in indices)
            if is_consistent(guess):
                return guess

            i = 0
            while i < length and indices[i] == base - 1:
                indices[i] = 0
                i += 1
            if i == length:
                break
            indices[i] += 1


SUBSEQS = [
    "319",
    "680",
    "180",
    "690",
    "129",
    "620",
    "762",
    "689",
    "762",
    "318",
    "368",
    "710",
    "720",
    "710",
    "629",
    "168",
    "160",
    "689",
    "716",
    "731",
    "736",
    "729",
    "316",
    "729",
    "729",
    "710",
    "769",
    "290",
    "719",
    "680",
    "318",
    "389",
    "162",
    "289",
    "162",
    "718",
    "729",
    "319",
    "790",
    "680",
    "890",
    "362",
    "319",
    "760",
    "316",
    "729",
    "380",
    "319",
    "728",
    "716",
]

if __name__ == "__main__":
    print(solution())
