"""Solution for 2025 star 5.

Problem page:
    https://adventofcode.com/2025/day/3

Solutions:
    1. Brute force
        - O(m * n^2) time, O(1) auxiliary space,
            where m = number of lines,
                  n = length of each line
    2. Greedy
        - O(mn) time, O(1) auxiliary space
"""

from aoclibs.hofs import compose, mapf
from aoclibs.executions import SolutionModule


def run(banks: list[list[int]]) -> int:
    """Find the sum of the maximum joltage possible from each bank."""
    ans = 0

    for bank in banks:
        n = len(bank)
        fst, snd = bank[0], bank[1]

        for i in range(2, n):
            battery = bank[i]

            if snd > fst:
                fst, snd = snd, battery
            elif battery >= snd:
                fst, snd = max(fst, snd), battery

        ans += fst * 10 + snd

    return ans


solution = SolutionModule(run=run)
solution.parser = compose(mapf(mapf(int)), str.splitlines)
