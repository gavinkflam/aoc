"""Solution for 2024 star 17.

Problem page:
    https://adventofcode.com/2024/day/9

Solutions:
    1. Brute force
        - O(n + k^2) time, O(k) auxiliary space
            where k = number of blocks
    2. Two pointers
        - O(n + k) time, O(1) auxiliary space
    3. Two pointers + optimizations
        - O(n) time, O(1) auxiliary space
        - Optimizations:
            1. Use Gauss summation to speed up checksum calculation
"""

from aoclibs.executions import SolutionModule
from aoclibs.hofs import mapf


def run(disk: list[int]) -> int:
    """Calculate the checksum of the disk after compacting the blocks."""
    n, checksum = len(disk), 0
    pos, lo, hi = 0, 0, n - 1

    while lo <= hi:
        is_file = lo % 2 == 0

        if is_file:
            file_id = lo // 2
            pos_sum = (2 * pos + disk[lo] - 1) * disk[lo] // 2

            checksum += file_id * pos_sum
            pos += disk[lo]
            lo += 1
        else:
            file_id = hi // 2
            moving = min(disk[lo], disk[hi])
            pos_sum = (2 * pos + moving - 1) * moving // 2

            checksum += file_id * pos_sum
            pos += moving
            # Track remaining blocks in-place to promote readability
            # These can be variables to avoid in-place modifications
            disk[lo], disk[hi] = disk[lo] - moving, disk[hi] - moving

            if disk[lo] == 0:
                lo = lo + 1
            if disk[hi] == 0:
                hi -= 2

    return checksum


solution = SolutionModule(run=run)
solution.parser = mapf(int)
