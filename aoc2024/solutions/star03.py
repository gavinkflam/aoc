"""Solution for 2024 star 3.

Problem page:
    https://adventofcode.com/2024/day/2

Solutions:
    1. Simple iteration
        - O(rows * cols) time, O(1) auxiliary space
"""

from aoclibs import inputs


def is_safe_report(report: list[int]) -> bool:
    """Determine is the given report safe."""
    cols = len(report)
    direction = 1 if report[1] > report[0] else -1

    for col in range(1, cols):
        curr, prev = report[col], report[col - 1]
        if not 1 <= (curr - prev) * direction <= 3:
            return False

    return True


def run(grid: list[list[int]]) -> int:
    """Count the number of safe reports."""
    rows = len(grid)
    safe_reports = 0

    for row in range(rows):
        if is_safe_report(grid[row]):
            safe_reports += 1

    return safe_reports


PARSER = inputs.parse_int_grid
PRINTER = str
