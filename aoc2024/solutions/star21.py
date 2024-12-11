"""Solution for 2024 star 21.

Problem page:
    https://adventofcode.com/2024/day/11

Solutions:
    1. Simulation, brute force
        - O(n^2 * 2^k) time, O(n) auxiliary space
            where k = number of blinks
    2. Simulation, stack
        - O(n * 2^k) time, O(n) auxiliary space
"""

import math

from aoclibs import inputs


def run(stones: list[int]) -> int:
    """Find out how many stones are there afte 25 blinks."""
    for _ in range(25):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif math.ceil(math.log(stone + 1, 10)) % 2 == 0:
                s = str(stone)
                mid = len(s) // 2

                new_stones.append(int(s[:mid]))
                new_stones.append(int(s[mid:]))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


PARSER = inputs.parse_int_line
PRINTER = str
