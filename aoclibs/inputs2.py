"""Version 2 composable helper functions to parse input files."""

from functools import reduce
from typing import Any, Callable, Pattern, Sequence


def identity(x: Any) -> Any:
    """Return the argument without modifications."""
    return x


def compose(*functions: Callable) -> Callable[[str], Any]:
    """Compose the provided functions into a single function."""
    return lambda arg: reduce(lambda acc, f: f(acc), reversed(functions), arg)


def ith(i: int) -> Callable[[Sequence[Any]], Any]:
    """Return a function that accept an argument and return the ith element of it."""
    return lambda xs: xs[i]


def applyf(fn: Callable) -> Callable[[list[Any]], Any]:
    """Return a function that accept a list, to pass the list as arguments to fn."""
    return lambda xs: fn(*xs)


def mapf(fn: Callable) -> Callable[[Any], list[Any]]:
    """Return a function that accept a list, to apply fn to each element."""
    return lambda ls: [fn(x) for x in ls]


def splitf(sep: str, fn: Callable = identity) -> Callable[[str], list[Any]]:
    """Return a function that accept a string, to split the string by sep and apply fn."""
    return lambda s: [fn(x) for x in s.split(sep)]


def re_splitf(
    pattern: Pattern, fn: Callable = identity, remove_empty_elements=False
) -> Callable[[str], list[Any]]:
    """Return a function that accept a string, to split the string using pattern and apply fn."""
    return lambda s: [
        fn(x) for x in pattern.split(s) if not (remove_empty_elements and x == "")
    ]


def re_mapf(pattern: Pattern, fn: Callable = identity) -> Callable[[str], list[Any]]:
    """Return a function that accept a string, to apply fn to each match of pattern."""
    return lambda s: [fn(x) for x in pattern.findall(s)]


def list_split(sep: Any) -> Callable[[Any], list[list[Any]]]:
    """Return a function that accept a list, to split it by sep."""

    def inner(ls: list[Any]) -> list[list[Any]]:
        parts, part = [[]], 0

        for e in ls:
            if e == sep:
                parts.append([])
                part += 1
            else:
                parts[-1].append(e)

        return parts

    return inner


def split_take_n(n: int) -> Callable[[Sequence], list[Sequence]]:
    """Return a function that accept a sequence,
    to split it into two parts with a first part of length n."""
    return lambda ls: [ls[:n], ls[n:]]


def split_but_n(n: int) -> Callable[[Sequence], list[Sequence]]:
    """Return a function that accept a sequence,
    to split it into two parts with a second part of length n."""
    return lambda ls: [ls[: len(ls) - n], ls[len(ls) - n :]]


def zip_applyf(*functions: Callable) -> Callable[[Any], list[list[Any]]]:
    """Return a function that accept a list,
    apply functions of the corresponding index to each element."""
    return lambda ls: [functions[i](x) for i, x in enumerate(ls)]
