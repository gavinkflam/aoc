"""Solution for 2024 star 24.

Problem page:
    https://adventofcode.com/2024/day/12#part2

Solutions:
    1. DFS + bitmasking
        - O(mn) time, O(mn) auxiliary space
"""

from aoclibs.executions import SolutionModule


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
UNVISITED = -1


def run(grid: list[str]) -> int:
    """Calculate the total cost of fences."""
    rows, cols = len(grid), len(grid[0])
    costs = 0

    visited = [[UNVISITED] * cols for _ in range(rows)]
    borders = [[0] * cols for _ in range(rows)]

    def visit_area(plant: str, row: int, col: int, step: int) -> tuple[int, int]:
        area, sides = 1, 0

        # Find all borders
        for direction, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant):
                sides += 1
                borders[row][col] |= 1 << direction

        # Visit neighbors
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant):
                continue

            if visited[nr][nc] != UNVISITED:
                # Only deduct from cells being visited earlier to avoid double counting
                if step < visited[nr][nc]:
                    sides -= (borders[row][col] & borders[nr][nc]).bit_count()
                continue

            visited[nr][nc] = step + 1
            n_area, n_sides = visit_area(plant, nr, nc, step + 1)
            area += n_area

            # Adjust for continuous borders
            sides += n_sides - (borders[row][col] & borders[nr][nc]).bit_count()

        return (area, sides)

    for row in range(rows):
        for col in range(cols):
            if visited[row][col] != UNVISITED:
                continue

            visited[row][col] = 0
            area, sides = visit_area(grid[row][col], row, col, 0)
            costs += area * sides

    return costs


solution = SolutionModule(run=run)
solution.parser = str.splitlines
