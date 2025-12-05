"""Solution for 2025 star 9.

Problem page:
    https://adventofcode.com/2025/day/5

Solutions:
    1. Brute force
        - O(mn) time, O(1) auxiliary space,
            where m = number of fresh ingredient ranges,
                  n = number of available ingredients
    2. Sorting + binary search
        - O(mlogm + nlogm) time, O(n) auxiliary space
    3. Sorting + two pointers
        - O(mlogm + nlogn + n) time, O(m + n) auxiliary space
"""

from aoclibs import inputs


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    """Parse inventory management system database input."""
    i = 0
    ranges, inventory = [], []

    # Parse fresh ingredient ranges
    while len(lines[i]) > 0:
        lo, hi = lines[i].split("-")
        ranges.append((int(lo), int(hi)))
        i += 1

    # Parse available ingredient ids
    i += 1

    while i < len(lines):
        inventory.append(int(lines[i]))
        i += 1

    return (ranges, inventory)


def run(lines: list[str]) -> int:
    """Count number of available fresh ingredients."""
    ans = 0

    # Prepare sorted ranges and inventory
    ranges, inventory = parse_input(lines)
    ranges.sort()
    inventory.sort()

    # Lookup freshness using two pointers
    m = len(ranges)
    i = 0

    for query in inventory:
        while i < m and ranges[i][1] < query:
            i += 1

        if i < m and ranges[i][0] <= query <= ranges[i][1]:
            ans += 1

    return ans


PARSER = inputs.parse_str_lines
PRINTER = str
