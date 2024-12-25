"""Helper functions related to output manipulation."""


def stringify_list(vals: list[any]) -> str:
    """Return a comma separated string of the given values."""
    return ",".join(str(val) for val in vals)
