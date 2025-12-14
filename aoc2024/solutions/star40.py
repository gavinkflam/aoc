"""Solution for 2024 star 40.

Problem page:
    https://adventofcode.com/2024/day/20#part2

Solutions:
    1. BFS + brute force
        - O(mn * mn) time, O(mn) auxiliary space
    2. BFS
        - O(mn * k^2) time, O(mn + k^2) auxiliary space
            where k = maximum cheat time
"""

from aoc2024.solutions import star39
from aoc2024.solutions.star39 import Coord, DIRECTIONS, Maze, VisitOrders
from aoclibs.executions import SolutionModule


MAX_CHEAT_TIME = 20
GOOD_CHEAT_THRESHOLD = 100


def count_good_cheats(
    maze: Maze, start: Coord, orders: VisitOrders, threshold: int
) -> int:
    """Count the number of good cheats."""
    rows, cols = len(maze), len(maze[0])

    def good_cheats_from(row: int, col: int) -> int:
        good_cheats = 0
        queue, visited = [(row, col)], set([(row, col)])

        for _ in range(MAX_CHEAT_TIME):
            new_queue = []

            for qr, qc in queue:
                for dr, dc in DIRECTIONS:
                    er, ec = qr + dr, qc + dc
                    if not (0 <= er < rows and 0 <= ec < cols):
                        continue
                    if (er, ec) in visited:
                        continue

                    visited.add((er, ec))
                    new_queue.append((er, ec))

                    if star39.savings(maze, orders, (row, col), (er, ec)) >= threshold:
                        good_cheats += 1

            queue = new_queue
            if not queue:
                break

        return good_cheats

    # Try all cheating options from each cell on the track
    row, col = start
    good_cheats = 0

    while maze[row][col] != "E":
        good_cheats += good_cheats_from(row, col)

        # Find next cell on the track
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if orders[nr][nc] > orders[row][col]:
                row, col = nr, nc
                break

    return good_cheats


def run(maze: Maze) -> int:
    """Find the number of cheats that can save at least 100 picoseconds."""
    start = star39.find_start(maze)
    orders = star39.find_visit_orders(maze, start)
    return count_good_cheats(maze, start, orders, threshold=GOOD_CHEAT_THRESHOLD)


solution = SolutionModule(run=run)
solution.parser = str.splitlines
