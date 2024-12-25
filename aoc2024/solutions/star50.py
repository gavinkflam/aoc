"""Solution for 2024 star 50.

Problem page:
    https://adventofcode.com/2024/day/25#part2

Solutions:
    1. Celebrate!
        - O(1) time, O(1) auxiliary space
"""

from aoclibs import inputs


def run(_: list[str]) -> int:
    """Happy 2025!"""
    return "*" * 50


PARSER = inputs.parse_str_lines
PRINTER = str
