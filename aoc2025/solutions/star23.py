"""Solution for 2025 star 23.

Problem page:
    https://adventofcode.com/2025/day/12

Solutions:
    1. Math
        - O(qm) time, O(1) auxiliary space,
            where q = number of region queries,
                  m = number of presents
                  
"""

from aoclibs import patterns
from aoclibs.hofs import (
    compose,
    ith,
    mapf,
    re_mapf,
    seq_slice,
    seq_split,
    split_but_n,
    zip_applyf,
)


def run(summary: tuple[list[list[str]], list[list[int]]]) -> int:
    """Find the number of areas that can fit all the listed presents."""
    ans = 0
    _, areas = summary

    for area in areas:
        width, height, quantities = area[0], area[1], area[2:]
        horizontal_slots, vertical_slots = width // 3, height // 3

        if sum(quantities) <= horizontal_slots * vertical_slots:
            ans += 1

    return ans


PARSER = compose(
    tuple,
    zip_applyf(
        mapf(seq_slice(1)),
        compose(mapf(re_mapf(patterns.UNSIGNED_INT, int)), ith(0)),
    ),
    split_but_n(1),
    seq_split(""),
    str.splitlines,
)
PRINTER = str
