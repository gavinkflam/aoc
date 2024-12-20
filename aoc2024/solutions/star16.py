"""Solution for 2024 star 16.

Problem page:
    https://adventofcode.com/2024/day/8#part2

Solutions:
    1. Hash map + hash set, brute force
        - O(mn + k^2 * max(m, n)) time, O(k) auxiliary space
            where k = number of antenna
"""

from aoc2024.solutions import star15
from aoclibs import inputs


def run(grid: list[list[str]]) -> int:
    """Count the number of unique locations that contain an antinode."""
    rows, cols = len(grid), len(grid[0])
    antennas = star15.find_antennas(grid)
    antinodes = set()

    for locations in antennas.values():
        k = len(locations)
        if k == 1:
            continue

        for i in range(k - 1):
            row_i, col_i = locations[i][0], locations[i][1]

            for j in range(i + 1, k):
                dr, dc = locations[j][0] - row_i, locations[j][1] - col_i
                nr, nc = row_i + dr, col_i + dc

                while 0 <= nr < rows and 0 <= nc < cols:
                    antinodes.add((nr, nc))
                    nr, nc = nr + dr, nc + dc

                nr, nc = row_i, col_i
                while 0 <= nr < rows and 0 <= nc < cols:
                    antinodes.add((nr, nc))
                    nr, nc = nr - dr, nc - dc

    return len(antinodes)


PARSER = inputs.parse_char_grid
PRINTER = str
