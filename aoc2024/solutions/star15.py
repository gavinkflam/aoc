"""Solution for 2024 star 15.

Problem page:
    https://adventofcode.com/2024/day/8

Solutions:
    1. Hash map + hash set, brute force - O(mn + k^2) time, O(k) auxiliary space
        where k = number of antenna
"""

from collections import defaultdict

from aoclibs import inputs


def find_antennas(grid: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    """Find the locations of all antennas grouped by frequency."""
    rows, cols = len(grid), len(grid[0])
    antennas = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch != ".":
                antennas[ch].append((r, c))

    return antennas


def run(grid: list[list[str]]) -> int:
    """Count the number of unique locations that contain an antinode."""
    rows, cols = len(grid), len(grid[0])
    antennas = find_antennas(grid)
    antinodes = set()

    for locations in antennas.values():
        k = len(locations)
        if k == 1:
            continue

        for i in range(k - 1):
            row_i, col_i = locations[i][0], locations[i][1]

            for j in range(i + 1, k):
                dr, dc = locations[j][0] - row_i, locations[j][1] - col_i
                nr, nc = row_i + 2 * dr, col_i + 2 * dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    antinodes.add((nr, nc))

                nr, nc = row_i - dr, col_i - dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    antinodes.add((nr, nc))

    return len(antinodes)


PARSER = inputs.parse_char_grid
PRINTER = str
