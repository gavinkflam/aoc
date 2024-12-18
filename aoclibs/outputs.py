"""Helper functions related to output manipulation."""


def stringify_integer_list(vals: list[int]) -> str:
    """Return a comma separated string of the given values."""
    return ",".join(str(val) for val in vals)
