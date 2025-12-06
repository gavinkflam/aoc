"""Solution for 2024 star 9.

Problem page:
    https://adventofcode.com/2024/day/5

Solutions:
    1. Hash map + hash set
        - O(kp^2 + n) time, O(n) auxiliary space
            where n = number of page rules,
                k = number of updates,
                p = max pages in an update
    2. Hash map + hash set, linear time
        - O(n + kp) time, O(n) auxiliary space
"""

from collections import defaultdict
from dataclasses import dataclass

from aoclibs import inputs2


@dataclass
class Instructions:
    """Data class to represent the parsed instructions."""

    rules: list[list[int]]
    updates: list[list[int]]

    def group_rules_by_leader(self) -> dict[int, set[int]]:
        """Return a dictionary of leader to a set of its followers."""
        groups = defaultdict(set)

        for x, y in self.rules:
            groups[x].add(y)

        return groups


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


def run(instructions: Instructions) -> int:
    """Find valid updates, and sum up their middle page numbers."""
    mid_page_sum = 0

    for update in instructions.updates:
        if is_valid_update(instructions.group_rules_by_leader(), update):
            mid_page_sum += update[len(update) // 2]

    return mid_page_sum


PARSER = inputs2.compose(
    inputs2.applyf(Instructions),
    inputs2.zip_applyf(
        inputs2.mapf(inputs2.compose(inputs2.mapf(int), inputs2.splitf("|"))),
        inputs2.mapf(inputs2.compose(inputs2.mapf(int), inputs2.splitf(","))),
    ),
    inputs2.list_split(""),
    str.splitlines,
)
PRINTER = str
