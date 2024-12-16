"""Solution for 2024 star 32.

Problem page:
    https://adventofcode.com/2024/day/16#part2

Solutions:
    1. Brute force, backtracking
        - O(5^mn) time, O(mn) auxiliary space
    2. Dijkstra's algorithm + BFS / DFS
        - O(mn * logmn + mn) time, O(mn) auxiliary space
"""

from collections import deque
import heapq

from aoc2024.solutions import star31
from aoc2024.solutions.star31 import DIRECTIONS, EAST
from aoclibs import inputs


UNVISITED = 1 << 32 - 1


def find_best_paths(maze: list[list[str]]) -> list[list[list[int]]]:
    """Use Dijkstra's algorithm to find the best paths to finish the maze."""
    rows, cols = len(maze), len(maze[0])
    sr, sc = star31.find_cell(maze, target="S")

    # Dijkstra's algorithm
    heap = [(0, sr, sc, EAST)]
    visited = [[[UNVISITED] * 4 for _ in range(cols)] for _ in range(rows)]
    visited[sr][sc][EAST] = 0

    while heap:
        score, row, col, direction = heapq.heappop(heap)

        if maze[row][col] == "E":
            return visited

        for new_dir, (dr, dc) in enumerate(DIRECTIONS):
            # Move one step in the same direction or turn without advancing
            if direction == new_dir:
                nr, nc, new_score = row + dr, col + dc, score + 1
            else:
                nr, nc, new_score = row, col, score + 1000

            if maze[nr][nc] == "#":
                continue
            if visited[nr][nc][new_dir] <= new_score:
                continue

            visited[nr][nc][new_dir] = new_score
            heapq.heappush(heap, (new_score, nr, nc, new_dir))

    return visited


def count_good_spots(maze: list[list[str]], scores: list[list[list[int]]]) -> int:
    """Count the number of cells on any best paths."""
    rows, cols = len(maze), len(maze[0])

    # Find all the directions entering the ending cell using any best paths
    er, ec = star31.find_cell(maze, target="E")
    visited = [[0] * cols for _ in range(rows)]
    queue = deque()

    for direction in range(4):
        if scores[er][ec][direction] == UNVISITED:
            continue
        visited[er][ec] ^= 1 << direction
        queue.append((er, ec, direction))

    # Use BFS to trace the best paths backward
    good_spots = 1

    while queue:
        row, col, direction = queue.popleft()

        for new_dir, (dr, dc) in enumerate(DIRECTIONS):
            # Move one step in the same direction or turn without advancing
            if direction == new_dir:
                nr, nc = row - dr, col - dc
                target_score = scores[row][col][direction] - 1
            else:
                nr, nc = row, col
                target_score = scores[row][col][direction] - 1000

            if maze[nr][nc] == "#" or visited[nr][nc] & (1 << new_dir) != 0:
                continue
            if scores[nr][nc][new_dir] != target_score:
                continue

            if visited[nr][nc] == 0:
                good_spots += 1

            visited[nr][nc] ^= 1 << new_dir
            queue.append((nr, nc, new_dir))

    return good_spots


def run(maze: list[list[str]]) -> int:
    """Find the number of cells on the best paths to complete the maze."""
    scores = find_best_paths(maze)
    return count_good_spots(maze, scores)


PARSER = inputs.parse_char_grid
PRINTER = str
