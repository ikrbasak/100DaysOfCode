# https://projecteuler.net/problem=31
# https://github.com/ikrbasak/100DaysOfCode
# 27-01-2023


def solution():
    TOTAL = 200
    ways = [1] + [0] * TOTAL
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    return ways[-1]


if __name__ == "__main__":
    print(solution())
