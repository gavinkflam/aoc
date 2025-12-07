"""Solution for 2024 star 22.

Problem page:
    https://adventofcode.com/2024/day/11#part2

Solutions:
    1. Simulation, brute force
        - O(n^2 * 2^k) time, O(n) auxiliary space
            where k = number of blinks
    2. Simulation, stack
        - O(n * 2^k) time, O(n) auxiliary space
    3. Memo
        - O(n + m) time, O(m + k) auxiliary space
            where m = range of stone sizes
"""

import math

from aoclibs import inputs2


def blink(memo: dict[int, list[int]], stone: int, blinks: int) -> int:
    """Find out how many stones will there be after the given number of blinks."""
    if blinks == 0:
        return 1

    if stone not in memo:
        memo[stone] = [0] * 76
    elif memo[stone][blinks] > 0:
        return memo[stone][blinks]

    if stone == 0:
        memo[stone][blinks] = blink(memo, 1, blinks - 1)
    elif math.ceil(math.log(stone + 1, 10)) % 2 == 0:
        s = str(stone)
        mid = len(s) // 2
        memo[stone][blinks] = blink(memo, int(s[:mid]), blinks - 1)
        memo[stone][blinks] += blink(memo, int(s[mid:]), blinks - 1)
    else:
        memo[stone][blinks] = blink(memo, stone * 2024, blinks - 1)

    return memo[stone][blinks]


def run(stones: list[int]) -> int:
    """Find out how many stones are there afte 75 blinks."""
    memo = {}
    return sum(blink(memo, stone, 75) for stone in stones)


PARSER = inputs2.splitf(" ", int)
PRINTER = str
