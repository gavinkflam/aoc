"""Solution for 2025 star 10.

Problem page:
    https://adventofcode.com/2025/day/5#part2

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

from aoc2025.solutions import star09


def run(database: star09.InventoryDatabase) -> int:
    """Count number of fresh ingredients."""
    ans = 0
    max_seen = -1
    database.ranges.sort()

    for lo, hi in database.ranges:
        ans += max(0, hi - max(lo, max_seen + 1) + 1)
        max_seen = max(max_seen, hi)

    return ans


PARSER = star09.PARSER
PRINTER = str
