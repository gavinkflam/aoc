"""Solution for 2025 star 10.

Problem page:
    https://adventofcode.com/2025/day/5

Solutions:
    1. Brute force
        - O(m^2 * k^2) time, O(1) auxiliary space,
            where m = number of fresh ingredient ranges,
                  k = maximum size of fresh ingredient range
    2. Hash set
        - O(mk) time, O(mk) auxiliary space
    3. Sorting + greedy
        - O(mlogm) time, O(m) auxiliary space
"""

from aoclibs import inputs
from aoc2025.solutions import star09


def run(lines: list[str]) -> int:
    """Count number of fresh ingredients."""
    # Prepare sorted ranges
    ranges, _ = star09.parse_input(lines)
    ranges.sort()

    # Greedy
    ans = 0
    max_seen = -1

    for lo, hi in ranges:
        ans += max(0, hi - max(lo, max_seen + 1) + 1)
        max_seen = max(max_seen, hi)

    return ans


PARSER = inputs.parse_str_lines
PRINTER = str
