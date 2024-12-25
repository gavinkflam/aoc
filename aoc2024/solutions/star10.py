"""Solution for 2024 star 10.

Problem page:
    https://adventofcode.com/2024/day/5#part2

Solutions:
    1. Hash map + hash set + sorting
        - O(k(p^2 + plogp) + n) time, O(n + p)
            where n = number of page rules,
                k = number of updates,
                p = max pages in an update
    2. Hash map + hash set, linear time + sorting
        - O(n + kp + plogp) time, O(n + p) auxiliary space
"""

import functools

from aoclibs import inputs
from aoc2024.solutions import star09


def run(grid: list[list[int]]) -> int:
    """Find invalid updates, fix them, and sum up their middle page numbers."""
    rules, updates = star09.prepare_data(grid)
    mid_page_sum = 0

    for update in updates:
        if not star09.is_valid_update(rules, update):
            fixed_update = sorted(
                update,
                key=functools.cmp_to_key(lambda x, y: 1 if x in rules[y] else -1),
            )
            mid_page_sum += fixed_update[len(update) // 2]

    return mid_page_sum


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
