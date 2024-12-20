"""Solution for 2024 star 9.

Problem page:
    https://adventofcode.com/2024/day/5

Solutions:
    1. Hash map + hash set
        - O(kp^2 + n) time, O(n) auxiliary space
            where n = number of page rules,
                k = number of updates,
                p = max pages in an update
    2. Hash map + hash set, linear
        - O(n + kp) time, O(n) auxiliary space
"""

from collections import defaultdict

from aoclibs import inputs


def prepare_data(grid: list[list[int]]) -> tuple[dict[int, set[int]], list[list[int]]]:
    """Prepare page rules and updates from the input grid."""
    rules, updates = defaultdict(set), []
    i = 0

    while len(grid[i]) == 2:
        x, y = grid[i]
        rules[x].add(y)
        i += 1

    i += 1
    while i < len(grid):
        updates.append(grid[i])
        i += 1

    return (rules, updates)


def is_valid_update(rules: dict[int, set[int]], update: list[int]) -> bool:
    """Determine is the given update valid according to the page rules."""
    pages = len(update)
    banned = set()

    for i in range(pages - 1, -1, -1):
        page = update[i]
        if page in banned:
            return False
        banned.update(rules[page])

    return True


def run(grid: list[list[int]]) -> int:
    """Find valid updates, and sum up their middle page numbers."""
    rules, updates = prepare_data(grid)
    mid_page_sum = 0

    for update in updates:
        if is_valid_update(rules, update):
            mid_page_sum += update[len(update) // 2]

    return mid_page_sum


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
