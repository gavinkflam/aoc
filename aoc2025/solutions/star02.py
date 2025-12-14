"""Solution for 2025 star 2.

Problem page:
    https://adventofcode.com/2025/day/1#part2

Solutions:
    1. Simulation
        - O(n) time, O(1) auxiliary space,
            where n = number of lines
"""

from aoc2025.solutions import star01


def run(instructions: list[tuple[str, int]]) -> int:
    """Simulate dial turning and count number of times the dial passes zero."""
    dial, zeros = 50, 0

    for direction, movement in instructions:
        was_zero = dial == 0

        dial += star01.DIRECTIONS[direction] * movement
        zeros += (abs(dial) // 100) + (1 if dial <= 0 and not was_zero else 0)
        dial %= 100

    return zeros


PARSER = star01.PARSER
PRINTER = str
