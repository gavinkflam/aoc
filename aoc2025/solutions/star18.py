"""Solution for 2025 star 18.

Problem page:
    https://adventofcode.com/2025/day/9#part2

Solutions:
    1. Brute force
        - O(n^2 * k^2) time, O(k^2) auxiliary space,
            where n = number of red tiles,
                  k = maximum coordinate
    2. Bucket fill + DP
        - O(n^2 + k^2) time, O(k^2) auxiliary space
    3. Compress canvas + bucket fill + DP
        - O(n^2) time, O(n^2) auxiliary space
"""

from aoc2025.solutions import star17


UNSET, WHITE, RED, GREEN = -1, 0, 1, 2
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def compress_coordinates(
    tiles: list[list[int]],
) -> tuple[int, dict[int, int], list[list[int]]]:
    """Compress coordinates by their relative order against each order."""
    coords = list(set(coord for tile in tiles for coord in tile))
    coords.sort()
    canvas_size = len(coords) + 2

    inflate = {k + 1: v for k, v in enumerate(coords)}
    inflate[len(coords) + 1] = coords[-1] + 1

    deflate = {v: k + 1 for k, v in enumerate(coords)}
    compressed_tiles = [[deflate[y], deflate[x]] for x, y in tiles]

    return (canvas_size, inflate, compressed_tiles)


def draw_and_fill_canvas(canvas_size: int, tiles: list[list[int]]) -> list[list[int]]:
    """Make a new canvas. Draw all the red and green tiles."""
    canvas = [[-1] * canvas_size for _ in range(canvas_size)]

    for i, (tr, tc) in enumerate(tiles):
        # Draw the red tile
        canvas[tr][tc] = RED

        # Draw the green tiles connecting the two tiles
        pr, pc = tiles[i - 1]

        if tr == pr:
            for c in range(min(pc, tc) + 1, max(pc, tc)):
                if canvas[tr][c] == UNSET:
                    canvas[tr][c] = GREEN
        else:
            for r in range(min(pr, tr) + 1, max(pr, tr)):
                if canvas[r][tc] == UNSET:
                    canvas[r][tc] = GREEN

    # Bucket fill the area not bound by red and green tiles
    bucket_fill(canvas, 0, 0, WHITE)

    # Fill the area bound by red and green tiles
    for r in range(canvas_size):
        for c in range(canvas_size):
            if canvas[r][c] == UNSET:
                canvas[r][c] = GREEN

    return canvas


def bucket_fill(canvas: list[list[int]], r: int, c: int, color: int):
    """Bucket fill starting from (r, c) with color."""
    canvas_size = len(canvas)
    queue = [(r, c)]
    canvas[r][c] = color

    while queue:
        new_queue = []

        for tr, tc in queue:
            for dr, dc in DIRECTIONS:
                nr, nc = tr + dr, tc + dc

                if not (0 <= nr < canvas_size and 0 <= nc < canvas_size):
                    continue
                if canvas[nr][nc] != UNSET:
                    continue

                canvas[nr][nc] = color
                new_queue.append((nr, nc))

        queue = new_queue


def calculate_colored_area_sums(
    canvas_size: int, canvas: list[list[int]]
) -> list[list[int]]:
    """Calculate the area sum of the rectangles from origin to each cell."""
    area_sums = [[0] * canvas_size for _ in range(canvas_size)]

    for r in range(1, canvas_size):
        for c in range(1, canvas_size):
            area_sums[r][c] = (
                area_sums[r - 1][c]
                + area_sums[r][c - 1]
                - area_sums[r - 1][c - 1]
                + (1 if canvas[r][c] != WHITE else 0)
            )

    return area_sums


def run(tiles: list[list[int]]) -> int:
    """Find the largest rectangle using two red tiles as the opposite corners."""
    n = len(tiles)
    canvas_size, inflate, compressed_tiles = compress_coordinates(tiles)
    canvas = draw_and_fill_canvas(canvas_size, compressed_tiles)
    colored_area_sums = calculate_colored_area_sums(canvas_size, canvas)

    # Find max colored area
    max_colored_area = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            tile_i, tile_j = compressed_tiles[i], compressed_tiles[j]
            min_r, min_c = min(tile_i[0], tile_j[0]), min(tile_i[1], tile_j[1])
            max_r, max_c = max(tile_i[0], tile_j[0]), max(tile_i[1], tile_j[1])

            colored_area = (
                colored_area_sums[max_r][max_c]
                - colored_area_sums[min_r - 1][max_c]
                - colored_area_sums[max_r][min_c - 1]
                + colored_area_sums[min_r - 1][min_c - 1]
            )
            rectangle_area = (max_r - min_r + 1) * (max_c - min_c + 1)

            if colored_area == rectangle_area:
                inflated_area = (inflate[max_r] - inflate[min_r] + 1) * (
                    inflate[max_c] - inflate[min_c] + 1
                )
                max_colored_area = max(max_colored_area, inflated_area)

    return max_colored_area


PARSER = star17.PARSER
PRINTER = str
