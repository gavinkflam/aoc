"""Solution for 2024 star 43.

Problem page:
    https://adventofcode.com/2024/day/22

Solutions:
    1. Iteration
        - O(nk) time, O(1) auxiliary space
            where n = number of secrets,
                  k = number of generations
"""

from aoclibs import inputs2


MOD = 16777216


def evolve(secret: int) -> int:
    """Evolve the given secret to the next generation."""
    secret = (secret ^ (secret * 64)) % MOD
    secret = (secret ^ (secret // 32)) % MOD
    secret = (secret ^ (secret * 2048)) % MOD
    return secret


def run(secrets: list[int]) -> int:
    """Find the sum of each of the secret's 2000th generation."""
    evolve_sum = 0

    for secret in secrets:
        for _ in range(2000):
            secret = evolve(secret)
        evolve_sum += secret

    return evolve_sum


PARSER = inputs2.compose(inputs2.mapf(int), str.splitlines)
PRINTER = str
