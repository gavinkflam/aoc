"""Solution for 2025 star 2.

Problem page:
    https://adventofcode.com/2025/day/1

Solutions:
    1. Simulation
        - O(n) time, O(1) auxiliary space,
            where n = number of lines
"""

from aoc2025.solutions import star01
from aoclibs import inputs


def run(lines: list[str]) -> int:
    """Simulate dial turning and count number of times the dial passes zero."""
    dial, zeros = 50, 0

    for movement in star01.parse_instructions(lines):
        was_zero = dial == 0

        dial += movement
        zeros += (abs(dial) // 100) + (1 if dial <= 0 and not was_zero else 0)
        dial %= 100

    return zeros


PARSER = inputs.parse_str_lines
PRINTER = str
