"""Solution for 2024 star 4.

Problem page:
    https://adventofcode.com/2024/day/2#part2

Solutions:
    1. Brute force - O(rows * cols * cols) time, O(1) auxiliary space
    2. Prefix and suffix array - O(rows * cols) time, O(cols) auxiliary space
    3. Suffix array - O(rows * cols) time, O(cols) auxiliary space
"""

from aoclibs import inputs

def is_safe_report(report: list[int], direction: int) -> bool:
    """Determine is the given report safe by tolerating at most one bad level in each report."""
    cols = len(report)
    safe_from = [True] * (cols + 1)

    # Prepare suffix array
    for col in range(cols - 2, -1, -1):
        curr, right = report[col], report[col + 1]
        safe_from[col] = safe_from[col + 1] and 1 <= (right - curr) * direction <= 3

    # Safe by dropping the first level
    if safe_from[1]:
        return True

    # Try to drop each level
    for col in range(1, cols - 1):
        curr, prev, right = report[col], report[col - 1], report[col + 1]

        if safe_from[col + 1] and 1 <= (right - prev) * direction <= 3:
            return True
        if not 1 <= (curr - prev) * direction <= 3:
            return False

    # Safe by dropping the last level
    return True

def run(grid: list[list[int]]) -> int:
    """Count the number of safe reports by tolerating at most one bad level in each report."""
    rows = len(grid)
    safe_reports = 0

    for row in range(rows):
        if is_safe_report(grid[row], 1) or is_safe_report(grid[row], -1):
            safe_reports += 1

    return safe_reports

PARSER = inputs.parse_int_grid
PRINTER = str
