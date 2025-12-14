"""Solution for 2025 star 3.

Problem page:
    https://adventofcode.com/2025/day/2

Solutions:
    1. Brute force
        - O(nm) time, O(1) auxiliary space,
            where n = number of ranges,
                  m = maximum number
    2. Composition
        - O(n * (10 ** (log10(m) / 2))) time, O(1) auxiliary space
"""

import math

from aoclibs.executions import SolutionModule
from aoclibs.hofs import compose, mapf, str_splitf


def run(ranges: list[list[str]]) -> int:
    """Find the sum of the invalid IDs."""
    ans = 0

    for lo_str, hi_str in ranges:
        lo, hi = int(lo_str), int(hi_str)
        left_len = len(lo_str) // 2
        right_len = (len(lo_str) + 1) // 2

        exp = right_len
        i = int(lo_str[:left_len]) if left_len == right_len else 10 ** (exp - 1)
        curr = i * (10**exp) + i

        while curr <= hi:
            if curr >= lo:
                ans += curr

            i += 1
            exp = int(math.log10(i)) + 1
            curr = i * (10**exp) + i

    return ans


solution = SolutionModule(run=run)
solution.parser = compose(mapf(str_splitf("-")), str_splitf(","))
