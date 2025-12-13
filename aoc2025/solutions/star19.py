"""Solution for 2025 star 19.

Problem page:
    https://adventofcode.com/2025/day/10

Solutions:
    1. Brute force, DFS
        - O(m * 2^n * k) time, O(n + k) auxiliary space,
            where m = number of machines,
                  n = maximum number of buttons on a machine,
                  k = maximum number of indicator lights on a machine
        - Optimizations:
            a. Represent each light by a bit, and apply bitwise XOR as button clicks
"""

import math

from aoclibs.hofs import (
    compose,
    ith,
    mapf,
    seq_slice,
    split_take_n,
    str_splitf,
    zip_applyf,
)


def lights_to_bits(lights: str) -> int:
    """Convert lights string to an integer with each bit representing a light."""
    return sum(2**i for i, x in enumerate(lights) if x == "#")


def button_to_bits(button: list[int]) -> int:
    """Convert button effect to an integer with each bit representing a light."""
    return sum(2**x for x in button)


def min_button_clicks(target: int, buttons: list[int], button_idx: int = 0) -> int:
    """Find the minimum button clicks to achieve target."""
    n = len(buttons)

    if button_idx == n:
        return 0 if target == 0 else math.inf

    return min(
        min_button_clicks(target, buttons, button_idx + 1),
        min_button_clicks(target ^ buttons[button_idx], buttons, button_idx + 1) + 1,
    )


def run(manual: list[tuple[str, list[list[int]]]]) -> int:
    """Find the sum of fewest button clicks to configure all indicator lights."""
    ans = 0

    for lights, configs in manual:
        target = lights_to_bits(lights)
        buttons = [button_to_bits(button) for button in configs[:-1]]

        ans += min_button_clicks(target, buttons)

    return ans


PARSER = compose(
    mapf(
        compose(
            tuple,
            zip_applyf(
                compose(seq_slice(1, -1), ith(0)),
                compose(mapf(compose(str_splitf(",", int), seq_slice(1, -1)))),
            ),
            split_take_n(1),
            str_splitf(" "),
        ),
    ),
    str.splitlines,
)
PRINTER = str
