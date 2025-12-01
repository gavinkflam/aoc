"""Solution for 2025 star 1.

Problem page:
    https://adventofcode.com/2025/day/1

Solutions:
    1. Simulation
        - O(n) time, O(1) auxiliary space,
            where n = number of lines
"""

from aoclibs import inputs


def parse_instructions(lines: list[str]) -> list[int]:
    """Parse each instruction into the magnitude of required movement."""
    return [(-1 if line[0] == "L" else 1) * int(line[1:]) for line in lines]


def run(lines: list[str]) -> int:
    """Simulate dial turning and count number of times the dial points at zero."""
    dial, zeros = 50, 0

    for movement in parse_instructions(lines):
        dial = (dial + movement) % 100

        if dial == 0:
            zeros += 1

    return zeros


PARSER = inputs.parse_str_lines
PRINTER = str
