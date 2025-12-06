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

from dataclasses import dataclass

from aoclibs import inputs2


@dataclass
class InventoryDatabase:
    """Data class to represent the parsed inventory database."""

    ranges: list[tuple[int, int]]
    inventory: list[int]


def run(database: InventoryDatabase) -> int:
    """Count number of available fresh ingredients."""
    ans = 0
    database.ranges.sort()
    database.inventory.sort()

    # Lookup freshness using two pointers
    m = len(database.ranges)
    i = 0

    for query in database.inventory:
        while i < m and database.ranges[i][1] < query:
            i += 1

        if i < m and database.ranges[i][0] <= query <= database.ranges[i][1]:
            ans += 1

    return ans


PARSER = inputs2.compose(
    inputs2.applyf(InventoryDatabase),
    inputs2.zip_applyf(
        inputs2.mapf(inputs2.splitf("-", int)),
        inputs2.mapf(int),
    ),
    inputs2.list_split(""),
    str.splitlines,
)
PRINTER = str
