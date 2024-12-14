"""Solution for 2024 star 27.

Problem page:
    https://adventofcode.com/2024/day/14

Solutions:
    1. Simulation
        - O(mn + kr) time, O(mn) auxiliary space
            where k = number of seconds,
                  r = number of robots,
                  m = height,
                  n = width
    2. Math
        - O(r) time, O(1) auxiliary space
"""

from aoclibs import inputs


WIDTH, HEIGHT = 101, 103
W_HALF, H_HALF = WIDTH // 2, HEIGHT // 2


def run(robots: list[list[int]]) -> int:
    """Calculate the safety factor after 100 seconds."""
    counts = [0] * 4

    def quadrant(x: int, y: int) -> int:
        if x == W_HALF or y == H_HALF:
            return -1
        return min(x // W_HALF, 1) * 2 + min(y // H_HALF, 1)

    for px, py, vx, vy in robots:
        tx = (px + vx * 100) % WIDTH
        ty = (py + vy * 100) % HEIGHT
        q = quadrant(tx, ty)

        if q != -1:
            counts[q] += 1

    return counts[0] * counts[1] * counts[2] * counts[3]


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
