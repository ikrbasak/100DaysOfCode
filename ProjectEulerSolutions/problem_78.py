# https://projecteuler.net/problem=78
# https://github.com/ikrbasak/100DaysOfCode
# 05-02-2023

import itertools

MODULUS = 10**6


def solution():
    partitions = [1]
    for i in itertools.count(len(partitions)):
        item = 0
        for j in itertools.count(1):
            sign = -1 if j % 2 == 0 else +1
            index = (j * j * 3 - j) // 2
            if index > i:
                break
            item += partitions[i - index] * sign
            index += j
            if index > i:
                break
            item += partitions[i - index] * sign
            item %= MODULUS

        if item == 0:
            return str(i)
        partitions.append(item)


if __name__ == "__main__":
    print(solution())
