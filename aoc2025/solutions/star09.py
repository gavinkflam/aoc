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

from aoclibs.executions import SolutionModule
from aoclibs.hofs import applyf, compose, mapf, seq_split, str_splitf, zip_applyf


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


solution = SolutionModule(run=run)
solution.parser = compose(
    applyf(InventoryDatabase),
    zip_applyf(
        mapf(str_splitf("-", int)),
        mapf(int),
    ),
    seq_split(""),
    str.splitlines,
)
