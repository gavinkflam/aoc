"""Solution for 2024 star 39.

Problem page:
    https://adventofcode.com/2024/day/20

Solutions:
    1. BFS, backtracking
        - O(2^mn) time, O(mn) auxiliary space
    2. BFS
        - O(mn) time, O(mn) auxiliary space
"""

from aoclibs import inputs


GOOD_CHEAT_THRESHOLD = 100
UNVISITED = -1
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


Maze = list[list[str]]
Coord = tuple[int, int]
VisitOrders = list[list[int]]


def find_start(maze: Maze) -> Coord:
    """Find the coordinate of the start cell."""
    rows, cols = len(maze), len(maze[0])

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == "S":
                return (row, col)

    return (-1, -1)


def find_visit_orders(maze: Maze, start: Coord) -> list[list[int]]:
    """Find the visit order of each cell in the race track."""
    rows, cols = len(maze), len(maze[0])
    row, col = start

    orders = [[UNVISITED] * cols for _ in range(rows)]
    orders[row][col] = 0

    while maze[row][col] != "E":
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if not (maze[nr][nc] != "#" and orders[nr][nc] == UNVISITED):
                continue

            orders[nr][nc] = orders[row][col] + 1
            row, col = nr, nc
            break

    return orders


def savings(maze: Maze, orders: VisitOrders, start: Coord, end: Coord) -> int:
    """Find the number of picoseconds saved with the given cheat."""
    rows, cols = len(maze), len(maze[0])
    (sr, sc), (er, ec) = start, end

    if not (0 <= er < rows and 0 <= ec < cols and maze[er][ec] != "#"):
        return -1
    if orders[er][ec] < orders[sr][sc]:
        return -1

    dist = abs(er - sr) + abs(ec - sc)
    return orders[er][ec] - orders[sr][sc] - dist


def count_good_cheats(
    maze: Maze, start: Coord, orders: VisitOrders, threshold: int
) -> int:
    """Count the number of good cheats."""
    # BFS from each cell on the track
    good_cheats = 0
    row, col = start

    while maze[row][col] != "E":
        next_pos = None

        for dr1, dc1 in DIRECTIONS:
            for dr2, dc2 in DIRECTIONS:
                er, ec = row + dr1 + dr2, col + dc1 + dc2
                if savings(maze, orders, (row, col), (er, ec)) >= threshold:
                    good_cheats += 1

            nr, nc = row + dr1, col + dc1
            if orders[nr][nc] > orders[row][col]:
                next_pos = (nr, nc)

        row, col = next_pos

    return good_cheats


def run(maze: Maze) -> int:
    """Find the number of cheats that can save at least 100 picoseconds."""
    start = find_start(maze)
    orders = find_visit_orders(maze, start)
    return count_good_cheats(maze, start, orders, threshold=GOOD_CHEAT_THRESHOLD)


PARSER = inputs.parse_char_grid
PRINTER = str
