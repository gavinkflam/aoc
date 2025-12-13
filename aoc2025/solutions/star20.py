"""Solution for 2025 star 20.

Problem page:
    https://adventofcode.com/2025/day/10

Solutions:
    1. Brute force, DFS
        - O(m * 2^(n + j) * k) time, O(n + k) auxiliary space,
            where m = number of machines,
                  n = maximum number of buttons on a machine,
                  k = maximum number of indicator lights on a machine,
                  j = maximum sum of joltage requirements of a machine
    2. DFS
        - O(m * 2^n * k * log(j)) time, O(n + k) auxiliary space
        - Optimizations:
            a. Represent each light by a bit, and apply bitwise XOR as button clicks
            b. Pruning - pattern not achievable, or joltage too high
        - Credits: https://www.reddit.com/r/adventofcode/comments/1pk87hl/
"""

from aoc2025.solutions import star19


INF = 10**9
BIT_TO_POSITION = {2**i: i for i in range(64)}


def generate_ways_to_make_each_pattern(buttons: list[int]) -> dict[int, list[int]]:
    """Generate all button combinations and group by the pattern they are producing."""
    n = len(buttons)
    ways = {}

    def dfs(idx: int, pattern_mask: int, buttons_mask: int):
        # Base case
        if idx == n:
            if pattern_mask not in ways:
                ways[pattern_mask] = []

            ways[pattern_mask].append(buttons_mask)
            return

        # Click the current button
        dfs(idx + 1, pattern_mask ^ buttons[idx], buttons_mask ^ (2**idx))

        # Skip the current button
        dfs(idx + 1, pattern_mask, buttons_mask)

    dfs(0, 0, 0)
    return ways


def find_min_clicks_to_charge(
    ways: dict[int, list[int]], buttons: list[int], joltages: list[int]
) -> int:
    """Find minimum button clicks to achieve the required joltages."""
    # Base case
    if not any(joltages):
        return 0

    pattern_mask = sum(2**i for i, jolt in enumerate(joltages) if jolt % 2 == 1)

    # No button combinations can achieve pattern
    if pattern_mask not in ways:
        return INF

    # Utility function to find the minimum button clicks of a specific button combination
    def solve_combination(buttons_mask: int, joltages: list[int]) -> int:
        set_bits = 0

        # Find the new joltage requirements after clicking the combination of buttons
        while buttons_mask > 0:
            button_idx = BIT_TO_POSITION[buttons_mask & -buttons_mask]
            lights_bitmask = buttons[button_idx]

            while lights_bitmask > 0:
                light = BIT_TO_POSITION[lights_bitmask & -lights_bitmask]
                joltages[light] -= 1

                if joltages[light] < 0:  # Out of bound
                    return INF

                lights_bitmask &= lights_bitmask - 1

            set_bits += 1
            buttons_mask &= buttons_mask - 1

        # Since all joltages are now even, halve the required amount to save work
        return set_bits + 2 * find_min_clicks_to_charge(
            ways, buttons, [jolt // 2 for jolt in joltages]
        )

    # Explore all button combinations to achieve pattern
    min_clicks = INF

    for buttons_mask in ways[pattern_mask]:
        min_clicks = min(min_clicks, solve_combination(buttons_mask, list(joltages)))

    return min_clicks


def run(manual: list[tuple[str, list[list[int]]]]) -> int:
    """Find the sum of fewest button clicks to configure joltage levels."""
    ans = 0

    for _, configs in manual:
        buttons, joltages = configs[:-1], configs[-1]
        button_masks = [star19.button_to_bits(button) for button in buttons]
        ways = generate_ways_to_make_each_pattern(button_masks)
        ans += find_min_clicks_to_charge(ways, button_masks, joltages)

    return ans


PARSER = star19.PARSER
PRINTER = str
