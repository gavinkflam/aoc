"""Solution for 2024 star 23.

Problem page:
    https://adventofcode.com/2024/day/12

Solutions:
    1. DFS
        - O(mn) time, O(mn) auxiliary space
"""

from aoclibs.executions import SolutionModule


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def run(grid: list[str]) -> int:
    """Calculate the total cost of fences."""
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    costs = 0

    def visit_area(plant: str, row: int, col: int) -> tuple[int, int]:
        area, perimeter = 1, 0

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant):
                perimeter += 1
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            n_area, n_perimeter = visit_area(plant, nr, nc)
            area, perimeter = area + n_area, perimeter + n_perimeter

        return (area, perimeter)

    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                continue

            visited[row][col] = True
            area, perimeter = visit_area(grid[row][col], row, col)
            costs += area * perimeter

    return costs


solution = SolutionModule(run=run)
solution.parser = str.splitlines
