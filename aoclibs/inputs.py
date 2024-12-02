"""Helper functions related to input manipulation."""

def parse_int_grid(lines: str) -> list[list[int]]:
    """Parse the given string as a grid of integer values."""
    return [[int(s) for s in l.split()] for l in lines.splitlines()]
