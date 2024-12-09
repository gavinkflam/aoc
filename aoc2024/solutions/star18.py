"""Solution for 2024 star 18.

Problem page:
    https://adventofcode.com/2024/day/9#part2

Solutions:
    1. Brute force
        - O(k^2 + n) time, O(k) auxiliary space
            where k = number of blocks
    2. Better brute force
        - O(n^2 + n + k) time, O(n) auxiliary space
    4. Heap + optimizations
        - O(nlogn + n) time, O(n) auxiliary space
        - Use a heap to keep track of the leftmost free space of each block size
        - Use Gauss summation to speed up checksum calculation
"""

import heapq

from aoclibs import inputs


def run(disk: list[int]) -> int:
    """Calculate the checksum of the disk after compacting the blocks."""
    n, checksum = len(disk), 0

    # Prepare prefix sum and free space heaps
    psum, spaces = [0] * n, [[] for _ in range(10)]

    for i in range(1, n):
        psum[i] = psum[i - 1] + disk[i - 1]
        if i % 2 == 1:
            spaces[disk[i]].append(i)

    # Compact the disk
    def find_space(size: int, hi: int) -> tuple[int]:
        """Find leftmost space that can fit the block."""
        loc, space = hi, 0

        for s in range(size, 10):
            if spaces[s] and spaces[s][0] < loc:
                loc, space = spaces[s][0], s
        return (loc, space)

    for f in range((n - 1) // 2 * 2, -1, -2):
        file_id = f // 2

        # Add checksum
        loc, space = find_space(disk[f], f)
        pos_sum = (2 * psum[loc] + disk[f] - 1) * disk[f] // 2
        checksum += file_id * pos_sum

        # If the file is moved, update pos and spaces
        if loc != f:
            psum[loc] += disk[f]

            if space > disk[f]:
                heapq.heappush(spaces[space - disk[f]], loc)
            heapq.heappop(spaces[space])

    return checksum


PARSER = inputs.parse_digit_list
PRINTER = str
